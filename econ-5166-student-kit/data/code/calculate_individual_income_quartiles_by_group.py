"""Weighted individual-income (PINCP) quartiles for four state groups.

Source: 2024 ACS 1-Year PUMS, Person-level CSV files (psam_pXX.csv).
For each group the adult (AGEP >= 18) person records of its three
state-level areas are pooled into ONE distribution, and a single
Q1 / Q2 / Q3 is computed from that pooled distribution with PWGTP weights.
State-level quartiles are never computed or averaged.

Data-cleaning rules (2024 ACS PUMS Data Dictionary):
  * The state column in these files is named STATE (2-digit FIPS).
  * AGEP: keep AGEP >= 18.
  * PINCP: blank = "N/A (less than 15 years old)" -> treated as missing and
    excluded. Valid range is -19998 .. 4209995; -19998 is the bottom code
    ("loss of $19,998 or more"), so it is a valid value, not a missing code.
    Zero and negative incomes are kept. Non-numeric or out-of-range values
    are excluded and counted.
  * ADJINC: PINCP is multiplied by ADJINC / 1,000,000 to express income in
    2024 dollars (official PUMS practice; same convention as the project's
    household-income script). Records with missing/invalid ADJINC are excluded.
  * PWGTP: must be numeric and > 0; otherwise the record is excluded.

Weighted quantile definition (identical for all four groups):
  Sort records by income x_(1) <= ... <= x_(n) with weights w_(i).
  Let W = sum(w_i) and C_k = sum_{i<=k} w_(i).
  Q(p) = x_(k*), where k* = min{k : C_k >= p * W}.
  This is the inverse of the weighted empirical CDF (lower quantile, no
  interpolation), so the result is always an observed income value.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Configuration (relative paths from econ-5166-student-kit/)
# ---------------------------------------------------------------------------
KIT_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = KIT_DIR / "data" / "raw" / "2024 ACS 1-Year PUMS FTP"
OUT_DIR = KIT_DIR / "data" / "processed"
OUT_FILE = OUT_DIR / "[final]individual_income_quartiles_by_group.csv"

STATE_FILES = {
    "06": ("California", "csv_pca/psam_p06.csv"),
    "08": ("Colorado", "csv_pco/psam_p08.csv"),
    "11": ("District of Columbia", "csv_pdc/psam_p11.csv"),
    "15": ("Hawaii", "csv_phi/psam_p15.csv"),
    "22": ("Louisiana", "csv_pla/psam_p22.csv"),
    "23": ("Maine", "csv_pme/psam_p23.csv"),
    "25": ("Massachusetts", "csv_pma/psam_p25.csv"),
    "28": ("Mississippi", "csv_pms/psam_p28.csv"),
    "35": ("New Mexico", "csv_pnm/psam_p35.csv"),
    "50": ("Vermont", "csv_pvt/psam_p50.csv"),
    "54": ("West Virginia", "csv_pwv/psam_p54.csv"),
}

GROUPS = [
    ("Group A", "Highest white population share", ["50", "23", "54"]),
    ("Group B", "Lowest white population share", ["06", "11", "15"]),
    ("Group C", "Highest median household income (2024 ACS 1-Year, B19013)", ["11", "25", "08"]),
    ("Group D", "Lowest median household income (2024 ACS 1-Year, B19013)", ["28", "35", "22"]),
]

USE_COLS = ["STATE", "AGEP", "PINCP", "PWGTP", "ADJINC"]
PINCP_MIN, PINCP_MAX = -19998, 4209995
QUANTILES = {"Q1_Income": 0.25, "Q2_Income": 0.50, "Q3_Income": 0.75}
MIN_SAMPLE = 1000  # flag groups with fewer valid records than this


# ---------------------------------------------------------------------------
# 1. Reading
# ---------------------------------------------------------------------------
def load_state(st: str) -> pd.DataFrame:
    """Read one Person-level file (read-only, as strings to avoid silent casts)."""
    name, rel = STATE_FILES[st]
    path = RAW_DIR / rel
    if not path.exists():
        raise FileNotFoundError(f"Missing person file for {name}: {path}")
    df = pd.read_csv(path, usecols=USE_COLS, dtype=str, keep_default_na=False)
    bad_state = set(df["STATE"].unique()) - {st}
    if bad_state:
        raise ValueError(f"{path.name} contains unexpected STATE codes: {bad_state}")
    return df


def load_all_states() -> dict[str, pd.DataFrame]:
    return {st: load_state(st) for st in STATE_FILES}


# ---------------------------------------------------------------------------
# 2. Group selection (each group is built independently from raw data)
# ---------------------------------------------------------------------------
def build_group_raw(raw: dict[str, pd.DataFrame], states: list[str]) -> pd.DataFrame:
    return pd.concat([raw[st].copy() for st in states], ignore_index=True)


# ---------------------------------------------------------------------------
# 3. Cleaning
# ---------------------------------------------------------------------------
def clean_group(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Apply age, income and weight rules; return clean data and counts."""
    stats = {"raw_n": len(df)}

    age = pd.to_numeric(df["AGEP"], errors="coerce")
    adults = df[age >= 18].copy()
    stats["adult_n"] = len(adults)

    # PINCP: blank = N/A; also drop non-numeric / out-of-range values.
    pincp = pd.to_numeric(adults["PINCP"].str.strip().replace("", np.nan), errors="coerce")
    adjinc = pd.to_numeric(adults["ADJINC"].str.strip().replace("", np.nan), errors="coerce")
    stats["pincp_blank"] = int((adults["PINCP"].str.strip() == "").sum())
    income_ok = pincp.notna() & pincp.between(PINCP_MIN, PINCP_MAX) & adjinc.notna() & (adjinc > 0)
    stats["income_excluded"] = int((~income_ok).sum())

    pwgtp = pd.to_numeric(adults["PWGTP"].str.strip().replace("", np.nan), errors="coerce")
    weight_ok = pwgtp.notna() & (pwgtp > 0)
    stats["weight_excluded"] = int((income_ok & ~weight_ok).sum())  # counted after income rule

    keep = income_ok & weight_ok
    clean = pd.DataFrame({
        "STATE": adults.loc[keep, "STATE"].values,
        "PINCP_RAW": pincp[keep].values,
        "INCOME": pincp[keep].values * adjinc[keep].values / 1_000_000,
        "PWGTP": pwgtp[keep].values,
    })
    stats["valid_n"] = len(clean)
    stats["weight_sum"] = float(clean["PWGTP"].sum())
    stats["missing_share"] = stats["income_excluded"] / stats["adult_n"] if stats["adult_n"] else np.nan
    return clean, stats


# ---------------------------------------------------------------------------
# 4. Weighted quantile
# ---------------------------------------------------------------------------
def weighted_quantile(values: np.ndarray, weights: np.ndarray, p: float) -> float:
    """Inverse weighted empirical CDF: smallest x with cumulative weight >= p*W."""
    if len(values) == 0:
        raise ValueError("Cannot compute quantile of empty data")
    order = np.argsort(values, kind="mergesort")  # stable -> reproducible
    v, w = values[order], weights[order]
    cum = np.cumsum(w)
    k = int(np.searchsorted(cum, p * cum[-1], side="left"))
    return float(v[k])


def compute_group(clean: pd.DataFrame) -> dict:
    x, w = clean["INCOME"].to_numpy(float), clean["PWGTP"].to_numpy(float)
    return {name: round(weighted_quantile(x, w, p), 2) for name, p in QUANTILES.items()}


# ---------------------------------------------------------------------------
# 5. Validation
# ---------------------------------------------------------------------------
def validate_group(label: str, states: list[str], clean: pd.DataFrame, stats: dict, q: dict) -> list[str]:
    issues = []
    present = sorted(clean["STATE"].unique())
    if present != sorted(states) or len(states) != 3:
        issues.append(f"states present {present} != expected {sorted(states)}")
    if stats["valid_n"] == 0:
        issues.append("no valid observations")
    elif stats["valid_n"] < MIN_SAMPLE:
        issues.append(f"small sample ({stats['valid_n']})")
    if stats["missing_share"] > 0.05:
        issues.append(f"income missing share high ({stats['missing_share']:.1%})")
    if not (clean["PWGTP"] > 0).all() or clean["PWGTP"].isna().any():
        issues.append("invalid weight included")
    if clean["PINCP_RAW"].isna().any() or not clean["PINCP_RAW"].between(PINCP_MIN, PINCP_MAX).all():
        issues.append("invalid income included")
    if not (q["Q1_Income"] <= q["Q2_Income"] <= q["Q3_Income"]):
        issues.append("quartiles not monotone")
    return issues


def print_report(label: str, states: list[str], stats: dict, q: dict, clean: pd.DataFrame, issues: list[str]) -> None:
    names = "; ".join(STATE_FILES[s][0] for s in states)
    print(f"\n=== {label}: {names} ===")
    print(f"  Raw person records          : {stats['raw_n']:,}")
    print(f"  Adults (AGEP >= 18)         : {stats['adult_n']:,}")
    print(f"  Excluded: missing/invalid PINCP: {stats['income_excluded']:,} "
          f"(blank N/A: {stats['pincp_blank']:,})")
    print(f"  Excluded: invalid PWGTP     : {stats['weight_excluded']:,}")
    print(f"  Valid records               : {stats['valid_n']:,}")
    print(f"  Sum of PWGTP                : {stats['weight_sum']:,.0f}")
    print(f"  Zero-income kept            : {(clean['PINCP_RAW'] == 0).sum():,}; "
          f"negative kept: {(clean['PINCP_RAW'] < 0).sum():,}")
    by_state = clean.groupby("STATE").agg(n=("PWGTP", "size"), w=("PWGTP", "sum"))
    for st, r in by_state.iterrows():
        print(f"    {STATE_FILES[st][0]:<22} n={r.n:,}  weight={r.w:,.0f}")
    print(f"  Q1={q['Q1_Income']:,.2f}  Q2={q['Q2_Income']:,.2f}  Q3={q['Q3_Income']:,.2f}")
    print("  Validation:", "PASS" if not issues else "ISSUES -> " + "; ".join(issues))


def validate_output(path: Path) -> None:
    out = pd.read_csv(path)
    assert len(out) == 4, f"expected 4 rows, got {len(out)}"
    assert list(out["Group"]) == [g[0] for g in GROUPS]
    for _, r in out.iterrows():
        assert len(r["Included_States"].split("; ")) == 3
        assert r["Q1_Income"] <= r["Q2_Income"] <= r["Q3_Income"]
        assert r["Sample_Size"] > 0 and r["Weighted_Population"] > 0
    print(f"\nRe-read {path.name}: 4 rows, all checks passed.")


# ---------------------------------------------------------------------------
# 6. Output / main
# ---------------------------------------------------------------------------
def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = load_all_states()
    print("Person files used:", ", ".join(Path(f).name for _, f in STATE_FILES.values()))

    rows, all_issues = [], {}
    for label, desc, states in GROUPS:
        group_raw = build_group_raw(raw, states)
        clean, stats = clean_group(group_raw)
        q = compute_group(clean)
        issues = validate_group(label, states, clean, stats, q)
        print_report(label, states, stats, q, clean, issues)
        all_issues[label] = issues
        rows.append({
            "Group": label,
            "Group_Description": desc,
            "Included_States": "; ".join(STATE_FILES[s][0] for s in states),
            **q,
            "Sample_Size": stats["valid_n"],
            "Weighted_Population": int(stats["weight_sum"]),
        })

    if any(all_issues.values()):
        raise SystemExit(f"Validation failed: {all_issues}")

    pd.DataFrame(rows).to_csv(OUT_FILE, index=False)
    print(f"\nSaved {OUT_FILE.relative_to(KIT_DIR)}")
    validate_output(OUT_FILE)


if __name__ == "__main__":
    main()
