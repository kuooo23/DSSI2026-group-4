"""Calculate weighted 2024 ACS PUMS household-income quartiles for MA and MS."""

from __future__ import annotations

from bisect import bisect_left
from decimal import Decimal
import math
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "income_quartiles_2024.csv"
REQUIRED_COLUMNS = {"STATE", "TYPEHUGQ", "HINCP", "WGTP", "ADJINC"}
HINCP_NA_CODE = "bbbbbbb"
# The 2024 ACS PUMS data dictionary gives HINCP's numeric range as -59,999..9,999,999.
HINCP_MIN_VALID = -59_999
HINCP_MAX_VALID = 9_999_999
QUANTILES = {
    "Q1": Decimal("0.25"),
    "Median": Decimal("0.50"),
    "Q3": Decimal("0.75"),
}
STATE_FILES = (
    ("MA", 25, PROJECT_ROOT / "data" / "raw" / "csv_hma" / "psam_h25.csv"),
    ("MS", 28, PROJECT_ROOT / "data" / "raw" / "csv_hms" / "psam_h28.csv"),
)


def read_state_data(state: str, state_fips: int, path: Path) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"{state} 原始資料不存在：{path}")

    header = pd.read_csv(path, nrows=0).columns
    missing_columns = REQUIRED_COLUMNS.difference(header)
    if missing_columns:
        raise ValueError(f"{path.name} 缺少必要欄位：{sorted(missing_columns)}")

    data = pd.read_csv(
        path,
        usecols=sorted(REQUIRED_COLUMNS),
        dtype="string",
        keep_default_na=False,
        na_filter=False,
        low_memory=False,
    )
    data = data.loc[:, ["STATE", "TYPEHUGQ", "HINCP", "WGTP", "ADJINC"]]

    state_counts = data["STATE"].value_counts(dropna=False).sort_index()
    print(f"\n[{state}] 總筆數：{len(data):,}")
    print(f"[{state}] STATE 值與筆數：{state_counts.to_dict()}")
    print(
        f"[{state}] TYPEHUGQ 各類筆數："
        f"{data['TYPEHUGQ'].value_counts(dropna=False).sort_index().to_dict()}"
    )

    if set(state_counts.index) != {str(state_fips)}:
        raise ValueError(
            f"{path.name} 的 STATE 應全部為 {state_fips}，實際值為 {state_counts.to_dict()}"
        )

    return data


def parse_numeric(data: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(data[column], errors="coerce")


def weighted_quantile(
    incomes: list[Decimal], weights: list[Decimal], quantile: Decimal
) -> Decimal:
    if len(incomes) != len(weights):
        raise ValueError("收入值與權重數量不一致。")

    weight_by_income: dict[Decimal, Decimal] = {}
    for income, weight in zip(incomes, weights):
        weight_by_income[income] = weight_by_income.get(income, Decimal(0)) + weight

    sorted_incomes = sorted(weight_by_income)
    cumulative_weights: list[Decimal] = []
    cumulative_total = Decimal(0)
    for income in sorted_incomes:
        cumulative_total += weight_by_income[income]
        cumulative_weights.append(cumulative_total)

    threshold = quantile * cumulative_total
    return sorted_incomes[bisect_left(cumulative_weights, threshold)]


def process_state(
    state: str, state_fips: int, path: Path
) -> dict[str, object]:
    data = read_state_data(state, state_fips, path)
    total_rows = len(data)

    weight = parse_numeric(data, "WGTP")
    income = parse_numeric(data, "HINCP")
    adjustment = parse_numeric(data, "ADJINC")
    income_text = data["HINCP"].str.strip()
    income_na_code = income_text.str.lower().eq(HINCP_NA_CODE)
    income_blank = income_text.eq("")
    income_numeric = income.notna()
    unexpected_income = ~(income_blank | income_na_code | income_numeric)

    unexpected_tokens = sorted(data.loc[unexpected_income, "HINCP"].unique().tolist())
    if unexpected_tokens:
        raise ValueError(
            f"[{state}] HINCP 出現資料字典未確認的非數值代碼，未予刪除："
            f"{unexpected_tokens}"
        )

    out_of_range_income = income_numeric & (
        (income < HINCP_MIN_VALID) | (income > HINCP_MAX_VALID)
    )
    if out_of_range_income.any():
        values = sorted(data.loc[out_of_range_income, "HINCP"].unique().tolist())
        raise ValueError(
            f"[{state}] HINCP 出現超出 2024 ACS PUMS 字典範圍的數值，未予刪除：{values}"
        )

    print(
        f"[{state}] WGTP=0：{int((weight == 0).sum()):,}；"
        f"WGTP<0：{int((weight < 0).sum()):,}；"
        f"WGTP 非數值／空白：{int(weight.isna().sum()):,}"
    )
    print(
        f"[{state}] HINCP 空白：{int(income_blank.sum()):,}；"
        f"HINCP N/A 代碼 {HINCP_NA_CODE}：{int(income_na_code.sum()):,}；"
        f"HINCP 合法負收入：{int((income < 0).sum()):,}"
    )
    print(
        f"[{state}] ADJINC 空白／非數值／非有限值："
        f"{int((adjustment.isna() | ~adjustment.map(math.isfinite)).sum()):,}；"
        f"ADJINC <= 0：{int((adjustment.notna() & (adjustment <= 0)).sum()):,}"
    )

    keep_housing = data["TYPEHUGQ"].eq("1")
    after_housing = data.loc[keep_housing].copy()
    after_housing["WGTP_numeric"] = weight.loc[keep_housing]
    after_housing["WGTP_finite"] = weight.loc[keep_housing].map(math.isfinite)
    after_housing["HINCP_numeric"] = income.loc[keep_housing]
    after_housing["ADJINC_numeric"] = adjustment.loc[keep_housing]
    after_housing["ADJINC_finite"] = adjustment.loc[keep_housing].map(math.isfinite)
    after_housing["HINCP_blank"] = income_blank.loc[keep_housing]
    after_housing["HINCP_na_code"] = income_na_code.loc[keep_housing]

    keep_weight = after_housing["WGTP_finite"] & (
        after_housing["WGTP_numeric"] > 0
    )
    after_weight = after_housing.loc[keep_weight].copy()

    keep_income = after_weight["HINCP_numeric"].notna()
    after_income = after_weight.loc[keep_income].copy()

    keep_adjustment = after_income["ADJINC_finite"] & (
        after_income["ADJINC_numeric"] > 0
    )
    after_adjustment = after_income.loc[keep_adjustment].copy()

    adjusted_income: list[Decimal] = []
    valid_indices: list[int] = []
    invalid_adjusted_income = 0
    for row_index, row in after_adjustment.iterrows():
        income_value = Decimal(str(row["HINCP_numeric"]))
        adjustment_value = Decimal(str(row["ADJINC_numeric"]))
        adjusted_value = (
            Decimal(income_value) * adjustment_value / Decimal(1_000_000)
        )
        if not adjusted_value.is_finite():
            invalid_adjusted_income += 1
            continue
        valid_indices.append(row_index)
        adjusted_income.append(adjusted_value)

    cleaned = after_adjustment.loc[valid_indices].copy()
    cleaned["adjusted_income"] = adjusted_income

    if cleaned.empty:
        raise ValueError(f"[{state}] 清理後沒有可計算的家庭資料。")

    invalid_weight_count = int((~after_housing["WGTP_finite"]).sum())
    nonpositive_weight_count = int(
        (
            after_housing["WGTP_finite"]
            & (after_housing["WGTP_numeric"] <= 0)
        ).sum()
    )
    missing_income_count = int(after_weight["HINCP_blank"].sum())
    na_code_count = int(after_weight["HINCP_na_code"].sum())
    invalid_adjustment_count = int(
        (
            ~after_income["ADJINC_finite"]
            | (after_income["ADJINC_numeric"] <= 0)
        ).sum()
    )

    exclusions = {
        "非一般住宅單位（TYPEHUGQ != 1）": total_rows - len(after_housing),
        "WGTP 空白／非數值": invalid_weight_count,
        "WGTP <= 0": nonpositive_weight_count,
        "HINCP 空白": missing_income_count,
        f"HINCP N/A 代碼 {HINCP_NA_CODE}": na_code_count,
        "ADJINC 空白／非數值／<= 0": invalid_adjustment_count,
        "adjusted_income 非有限值": invalid_adjusted_income,
    }

    if sum(exclusions.values()) + len(cleaned) != total_rows:
        raise AssertionError(f"[{state}] 排除筆數重複或遺漏，請檢查逐步清理流程。")

    weights = [Decimal(str(value)) for value in cleaned["WGTP_numeric"]]
    if any(not value.is_finite() or value <= 0 for value in weights):
        raise AssertionError(f"[{state}] 清理後仍有非正數 WGTP。")

    quantiles = {
        name: weighted_quantile(
            cleaned["adjusted_income"].tolist(), weights, proportion
        )
        for name, proportion in QUANTILES.items()
    }
    q1 = quantiles["Q1"]
    median = quantiles["Median"]
    q3 = quantiles["Q3"]
    iqr = q3 - q1
    if not q1 <= median <= q3:
        raise AssertionError(f"[{state}] 四分位數次序錯誤：{quantiles}")
    if iqr != q3 - q1:
        raise AssertionError(f"[{state}] IQR 與 Q3 - Q1 不一致。")

    result: dict[str, object] = {
        "state": state,
        "state_fips": state_fips,
        "sample_size_before_cleaning": total_rows,
        "sample_size_after_cleaning": len(cleaned),
        "estimated_households": sum(weights, Decimal(0)),
        "Q1": q1,
        "Median": median,
        "Q3": q3,
        "IQR": iqr,
    }

    print(f"[{state}] 清理前樣本數：{total_rows:,}")
    print(f"[{state}] 逐項排除筆數（原因互斥，不重複計算）：")
    for reason, count in exclusions.items():
        print(f"  - {reason}：{count:,}")
    print(f"[{state}] 清理後樣本數：{len(cleaned):,}")
    print(
        f"[{state}] 清理後 WGTP 權重總和（estimated_households）："
        f"{sum(weights, Decimal(0)):,}"
    )
    print(
        f"[{state}] Q1={q1}；Median={median}；Q3={q3}；IQR={iqr}"
    )
    print(f"[{state}] 驗證 Q1 <= Median <= Q3：通過")
    print(f"[{state}] 驗證 IQR = Q3 - Q1：通過")

    return result


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    results: list[dict[str, object]] = []
    for state, state_fips, path in STATE_FILES:
        results.append(process_state(state, state_fips, path))

    output = pd.DataFrame(
        results,
        columns=[
            "state",
            "state_fips",
            "sample_size_before_cleaning",
            "sample_size_after_cleaning",
            "estimated_households",
            "Q1",
            "Median",
            "Q3",
            "IQR",
        ],
    )
    output.to_csv(OUTPUT_PATH, index=False)
    print(f"\n輸出 CSV 已建立：{OUTPUT_PATH}")

    verified = pd.read_csv(OUTPUT_PATH, dtype={"state": "string"})
    expected_states = ["MA", "MS"]
    if verified.columns.tolist() != output.columns.tolist():
        raise AssertionError(f"輸出欄位錯誤：{verified.columns.tolist()}")
    if len(verified) != 2 or verified["state"].tolist() != expected_states:
        raise AssertionError(
            f"輸出列數或州別錯誤：列數={len(verified)}，"
            f"州別={verified['state'].tolist()}"
        )
    if not verified.equals(output.astype({"state": "string"})):
        numeric_columns = [column for column in output.columns if column != "state"]
        for column in numeric_columns:
            verified_values = verified[column].map(lambda value: Decimal(str(value)))
            expected_values = output[column].map(lambda value: Decimal(str(value)))
            if not verified_values.equals(expected_values):
                raise AssertionError(f"重新讀取後欄位 {column} 的數值不一致。")
    print("重新讀取驗證：2 列（MA、MS）、欄位順序及數值均正確。")


if __name__ == "__main__":
    main()
