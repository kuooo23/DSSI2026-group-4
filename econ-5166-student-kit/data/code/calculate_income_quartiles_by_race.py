"""Compare weighted household-income quartiles by state white population share."""

from __future__ import annotations

import csv
import hashlib
import math
import os
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = PROJECT_ROOT / "data" / "raw"
OUTPUT_ROOT = PROJECT_ROOT / "data" / "processed"
RESULTS_PATH = OUTPUT_ROOT / "income_quartiles_by_race_2024.csv"
QUALITY_PATH = OUTPUT_ROOT / "income_quartiles_race_data_quality_report_2024.csv"
DATA_DICTIONARY_URL = (
    "https://www2.census.gov/programs-surveys/acs/tech_docs/pums/"
    "data_dict/PUMS_Data_Dictionary_2024.txt"
)
HINCP_NA_CODE = Decimal("-60000")
HINCP_MIN_VALID = Decimal("-59999")
HINCP_MAX_VALID = Decimal("9999999")
MILLION = Decimal("1000000")
QUANTILES = (
    ("Q1", Decimal("0.25")),
    ("Median", Decimal("0.50")),
    ("Q3", Decimal("0.75")),
)
REQUIRED_COLUMNS = {"STATE", "TYPEHUGQ", "HINCP", "WGTP", "ADJINC", "SERIALNO"}


@dataclass(frozen=True)
class StateSource:
    abbreviation: str
    name: str
    fips: str
    path: Path
    expected_sha256: str


@dataclass(frozen=True)
class CleanRecord:
    state: str
    hincp: Decimal
    adjinc: Decimal
    adjusted_income: Decimal
    wgtp: Decimal


@dataclass
class StateResult:
    source: StateSource
    sample_size_before_cleaning: int = 0
    state_counts: Counter[str] = field(default_factory=Counter)
    typehugq_counts: Counter[str] = field(default_factory=Counter)
    raw_weight_zero: int = 0
    raw_weight_negative: int = 0
    raw_weight_missing: int = 0
    raw_weight_invalid: int = 0
    raw_hincp_missing: int = 0
    raw_hincp_special: int = 0
    raw_hincp_negative: int = 0
    raw_adjinc_missing: int = 0
    raw_adjinc_invalid: int = 0
    raw_adjinc_nonpositive: int = 0
    invalid_serial_numbers: int = 0
    invalid_state_values: Counter[str] = field(default_factory=Counter)
    unexpected_hincp_tokens: Counter[str] = field(default_factory=Counter)
    out_of_range_hincp: Counter[str] = field(default_factory=Counter)
    fractional_hincp: Counter[str] = field(default_factory=Counter)
    exclusions: Counter[str] = field(default_factory=Counter)
    records: list[CleanRecord] = field(default_factory=list)

    @property
    def total_weight(self) -> Decimal:
        return sum((record.wgtp for record in self.records), Decimal(0))

SOURCES = (
    StateSource(
        "VT",
        "Vermont",
        "50",
        RAW_ROOT / "csv_hvt" / "psam_h50.csv",
        "a2817884910d3d0b5080c8503586253d411584e6d1256b15dca1cd2a3d45a357",
    ),
    StateSource(
        "ME",
        "Maine",
        "23",
        RAW_ROOT / "csv_hme" / "psam_h23.csv",
        "b1b1b8ca7d87e279b8560ca18ef2e2f79aba57d240112b6a85bc9ed0674c60be",
    ),
    StateSource(
        "WV",
        "West Virginia",
        "54",
        RAW_ROOT / "csv_hwv" / "psam_h54.csv",
        "3c4d704c36a5506923977bd3de3f80279e2bcb85c4155587b37a65f9dd48618f",
    ),
    StateSource(
        "CA",
        "California",
        "06",
        RAW_ROOT / "csv_hca" / "psam_h06.csv",
        "5fe1de62e12e356a2be9be237d3b9e3ea4f8c5e04e9969b4d9efa4a61b7098a4",
    ),
    StateSource(
        "DC",
        "District of Columbia",
        "11",
        RAW_ROOT / "csv_hdc" / "psam_h11.csv",
        "9cf40696496ce3abad416ec02d1d839a97291c5ad3d442b52f20e48e4589ec42",
    ),
    StateSource(
        "HI",
        "Hawaii",
        "15",
        RAW_ROOT / "csv_hhi" / "psam_h15.csv",
        "8b1f493afaa2f6abef8460bfa3638958dd26f3be7a2373d6ebe4554dd62bf5d7",
    ),
)
GROUPS = (
    ("High White Population Share", ("VT", "ME", "WV")),
    ("Low White Population Share", ("CA", "DC", "HI")),
)
SOURCE_BY_ABBREVIATION = {source.abbreviation: source for source in SOURCES}
RESULT_COLUMNS = (
    "race_group",
    "included_states",
    "sample_size_before_cleaning",
    "sample_size_after_cleaning",
    "estimated_households",
    "Q1",
    "Median",
    "Q3",
    "IQR",
)
QUALITY_COLUMNS = (
    "state",
    "state_fips",
    "sample_size_before_cleaning",
    "sample_size_after_cleaning",
    "excluded_typehugq",
    "excluded_invalid_weight",
    "excluded_missing_hincp",
    "excluded_special_code",
    "excluded_invalid_adjinc",
    "excluded_invalid_adjusted_income",
    "total_excluded",
    "total_weight_after_cleaning",
)
EXCLUSION_COLUMNS = (
    "excluded_typehugq",
    "excluded_invalid_weight",
    "excluded_missing_hincp",
    "excluded_special_code",
    "excluded_invalid_adjinc",
    "excluded_invalid_adjusted_income",
)


def parse_decimal(value: str | None) -> Decimal | None:
    if value is None or not value.strip():
        return None
    try:
        parsed = Decimal(value.strip())
    except InvalidOperation:
        return None
    return parsed if parsed.is_finite() else None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def format_decimal(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def process_source(source: StateSource) -> StateResult:
    result = StateResult(source=source)
    with source.path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.sample_size_before_cleaning += 1
            row_number = result.sample_size_before_cleaning + 1

            state_value = (row.get("STATE") or "").strip()
            result.state_counts[state_value] += 1
            if not state_value.isdigit() or int(state_value) != int(source.fips):
                result.invalid_state_values[state_value] += 1
            if not (row.get("SERIALNO") or "").strip().startswith("2024"):
                result.invalid_serial_numbers += 1

            typehugq = (row.get("TYPEHUGQ") or "").strip()
            result.typehugq_counts[typehugq] += 1

            weight_text = row.get("WGTP")
            weight = parse_decimal(weight_text)
            weight_value = "" if weight_text is None else weight_text.strip()
            if not weight_value:
                result.raw_weight_missing += 1
            elif weight is None:
                result.raw_weight_invalid += 1
            elif weight == 0:
                result.raw_weight_zero += 1
            elif weight < 0:
                result.raw_weight_negative += 1

            income_text = row.get("HINCP")
            income_string = "" if income_text is None else income_text.strip()
            income = parse_decimal(income_text)
            if not income_string:
                result.raw_hincp_missing += 1
            elif income is None:
                result.unexpected_hincp_tokens[income_string] += 1
            elif income == HINCP_NA_CODE:
                result.raw_hincp_special += 1
            elif income != income.to_integral_value():
                result.fractional_hincp[income_string] += 1
            elif income < HINCP_MIN_VALID or income > HINCP_MAX_VALID:
                result.out_of_range_hincp[income_string] += 1
            elif income < 0:
                result.raw_hincp_negative += 1

            adjustment_text = row.get("ADJINC")
            adjustment_string = (
                "" if adjustment_text is None else adjustment_text.strip()
            )
            adjustment = parse_decimal(adjustment_text)
            if not adjustment_string:
                result.raw_adjinc_missing += 1
            elif adjustment is None:
                result.raw_adjinc_invalid += 1
            elif adjustment <= 0:
                result.raw_adjinc_nonpositive += 1

            if None in row:
                raise ValueError(
                    f"{source.path.name} 第 {row_number} 列欄位數與標頭不符。"
                )
            if typehugq != "1":
                result.exclusions["excluded_typehugq"] += 1
                continue
            if weight is None or weight <= 0:
                result.exclusions["excluded_invalid_weight"] += 1
                continue
            if not income_string:
                result.exclusions["excluded_missing_hincp"] += 1
                continue
            if income == HINCP_NA_CODE:
                result.exclusions["excluded_special_code"] += 1
                continue
            if income is None:
                continue
            if adjustment is None or adjustment <= 0:
                result.exclusions["excluded_invalid_adjinc"] += 1
                continue

            with localcontext() as context:
                context.prec = 40
                adjusted_income = income * adjustment / MILLION
            if not adjusted_income.is_finite():
                result.exclusions["excluded_invalid_adjusted_income"] += 1
                continue

            result.records.append(
                CleanRecord(
                    state=state_value,
                    hincp=income,
                    adjinc=adjustment,
                    adjusted_income=adjusted_income,
                    wgtp=weight,
                )
            )

    print(f"\n[{source.name} ({source.abbreviation})] 原始總筆數：{result.sample_size_before_cleaning:,}")
    print(f"  STATE 分布：{dict(sorted(result.state_counts.items()))}")
    print(f"  TYPEHUGQ 各類筆數：{dict(sorted(result.typehugq_counts.items()))}")
    print(
        "  原始 WGTP："
        f"0={result.raw_weight_zero:,}；負數={result.raw_weight_negative:,}；"
        f"空值={result.raw_weight_missing:,}；其他無效數值={result.raw_weight_invalid:,}"
    )
    print(
        "  原始 HINCP："
        f"空值={result.raw_hincp_missing:,}；"
        f"字典 N/A 代碼 -60000={result.raw_hincp_special:,}；"
        f"合法負收入={result.raw_hincp_negative:,}"
    )
    print(
        "  原始 ADJINC："
        f"空值={result.raw_adjinc_missing:,}；"
        f"非數值／非有限值={result.raw_adjinc_invalid:,}；"
        f"<= 0={result.raw_adjinc_nonpositive:,}"
    )
    if result.unexpected_hincp_tokens:
        print(f"  未知 HINCP 代碼（未予推定或排除）：{dict(result.unexpected_hincp_tokens)}")
    if result.out_of_range_hincp:
        print(f"  超出字典範圍的 HINCP（未予推定或排除）：{dict(result.out_of_range_hincp)}")
    if result.fractional_hincp:
        print(f"  非整數 HINCP（未予推定或排除）：{dict(result.fractional_hincp)}")

    if result.invalid_state_values:
        raise ValueError(f"[{source.abbreviation}] STATE 與預期 FIPS 不符。")
    if result.invalid_serial_numbers:
        raise ValueError(f"[{source.abbreviation}] 發現非 2024 SERIALNO。")
    if (
        result.unexpected_hincp_tokens
        or result.out_of_range_hincp
        or result.fractional_hincp
    ):
        raise ValueError(
            f"[{source.abbreviation}] HINCP 含未確認或不符合字典範圍的值，停止處理。"
        )

    excluded_total = sum(result.exclusions.values())
    if excluded_total + len(result.records) != result.sample_size_before_cleaning:
        raise AssertionError(f"[{source.abbreviation}] 逐步排除筆數不守恆。")
    if not result.records:
        raise ValueError(f"[{source.abbreviation}] 清理後沒有有效家庭資料。")

    print("  逐步排除筆數（原因互斥）：")
    for column in EXCLUSION_COLUMNS:
        print(f"    {column}: {result.exclusions[column]:,}")
    print(f"  清理後筆數：{len(result.records):,}")
    print(f"  清理後 WGTP 總和：{result.total_weight:,}")
    return result


def weighted_empirical_quantile(
    records: list[CleanRecord], quantile: Decimal
) -> Decimal:
    if quantile <= 0 or quantile > 1:
        raise ValueError(f"分位數比例必須介於 (0, 1]：{quantile}")
    weights_by_income: defaultdict[Decimal, Decimal] = defaultdict(Decimal)
    for record in records:
        if not record.wgtp.is_finite() or record.wgtp <= 0:
            raise ValueError("加權分位數輸入含無效或非正數 WGTP。")
        weights_by_income[record.adjusted_income] += record.wgtp
    total_weight = sum(weights_by_income.values(), Decimal(0))
    threshold = total_weight * quantile
    cumulative_weight = Decimal(0)
    for income in sorted(weights_by_income):
        cumulative_weight += weights_by_income[income]
        if cumulative_weight >= threshold:
            return income
    raise AssertionError("累積權重未達到分位數門檻。")


def validate_source_files() -> None:
    missing: list[str] = []
    for source in SOURCES:
        if not source.path.is_file():
            missing.append(str(source.path))
        readme = source.path.parent / "ACS2024_PUMS_README.pdf"
        if not readme.is_file():
            missing.append(str(readme))
    if missing:
        raise FileNotFoundError(
            "缺少指定的 2024 ACS PUMS CSV 或 README，停止處理：\n"
            + "\n".join(missing)
        )

    expected_header: tuple[str, ...] | None = None
    for source in SOURCES:
        with source.path.open("r", newline="", encoding="utf-8-sig") as file:
            header = tuple(next(csv.reader(file), ()))
        if not header:
            raise ValueError(f"{source.path} 是空檔。")
        if len(header) != len(set(header)):
            raise ValueError(f"{source.path} 有重複欄名：{header}")
        if expected_header is None:
            expected_header = header
        elif header != expected_header:
            raise ValueError(f"{source.path} 的欄位名稱或順序與其他來源不一致。")
        missing_columns = REQUIRED_COLUMNS.difference(header)
        if missing_columns:
            raise ValueError(
                f"{source.path} 缺少必要欄位：{sorted(missing_columns)}"
            )
        actual_hash = sha256_file(source.path)
        if actual_hash != source.expected_sha256:
            raise ValueError(
                f"{source.path} SHA-256 與已核對版本不符，停止處理。"
            )

    print("六份資料皆有對應的 2024 PUMS README；CSV 欄位名稱與順序一致。")
    print(
        "PUMS 字典確認 HINCP -60000 為 GQ／空置單位 N/A；"
        "合法值為 -59999 至 9999999，負收入予以保留。"
    )


def calculate_group(
    label: str,
    abbreviations: tuple[str, ...],
    state_results: dict[str, StateResult],
) -> dict[str, str]:
    records = [
        record
        for abbreviation in abbreviations
        for record in state_results[abbreviation].records
    ]
    if not records:
        raise ValueError(f"{label} 清理後沒有有效家庭資料。")

    expected_fips = {
        SOURCE_BY_ABBREVIATION[abbreviation].fips
        for abbreviation in abbreviations
    }
    if {record.state for record in records} != expected_fips:
        raise AssertionError(f"{label} 合併後 STATE 欄位遺失或不符合預期。")

    total_weight = sum((record.wgtp for record in records), Decimal(0))
    quantiles = {
        name: weighted_empirical_quantile(records, proportion)
        for name, proportion in QUANTILES
    }
    q1 = quantiles["Q1"]
    median = quantiles["Median"]
    q3 = quantiles["Q3"]
    iqr = q3 - q1
    if not q1 <= median <= q3:
        raise AssertionError(f"{label} 四分位數順序錯誤：{quantiles}")
    if iqr != q3 - q1:
        raise AssertionError(f"{label} IQR 與 Q3 - Q1 不一致。")

    before = sum(
        state_results[abbreviation].sample_size_before_cleaning
        for abbreviation in abbreviations
    )
    included_states = "; ".join(
        SOURCE_BY_ABBREVIATION[abbreviation].name
        for abbreviation in abbreviations
    )
    row = {
        "race_group": label,
        "included_states": included_states,
        "sample_size_before_cleaning": str(before),
        "sample_size_after_cleaning": str(len(records)),
        "estimated_households": format_decimal(total_weight),
        "Q1": format_decimal(q1),
        "Median": format_decimal(median),
        "Q3": format_decimal(q3),
        "IQR": format_decimal(iqr),
    }

    print(f"\n{label}")
    print(f"  合併前原始樣本數：{before:,}")
    print(f"  合併後清理樣本數：{len(records):,}")
    print(f"  WGTP 總和：{total_weight:,}")
    print(
        f"  Weighted Empirical Quantile：Q1={q1}；Median={median}；"
        f"Q3={q3}；IQR={iqr}"
    )
    print(f"  驗證 Q1 <= Median <= Q3：{q1 <= median <= q3}")
    print(f"  驗證 IQR = Q3 - Q1：{iqr == q3 - q1}")
    print("  加權方法：收入排序後累加 WGTP；相同收入先合計權重。")
    return row


def build_quality_rows(
    state_results: dict[str, StateResult],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in SOURCES:
        result = state_results[source.abbreviation]
        exclusions = {
            column: result.exclusions[column] for column in EXCLUSION_COLUMNS
        }
        total_excluded = sum(exclusions.values())
        if total_excluded + len(result.records) != result.sample_size_before_cleaning:
            raise AssertionError(f"{source.name} 逐步排除筆數不守恆。")
        rows.append(
            {
                "state": source.name,
                "state_fips": source.fips,
                "sample_size_before_cleaning": str(result.sample_size_before_cleaning),
                "sample_size_after_cleaning": str(len(result.records)),
                **{column: str(exclusions[column]) for column in EXCLUSION_COLUMNS},
                "total_excluded": str(total_excluded),
                "total_weight_after_cleaning": format_decimal(result.total_weight),
            }
        )
    return rows


def write_csv_atomically(
    path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]
) -> None:
    handle, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary_name)
    try:
        with os.fdopen(handle, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=columns, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary_path, path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise


def read_and_validate_csv(
    path: Path, columns: tuple[str, ...], expected_rows: int
) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if tuple(reader.fieldnames or ()) != columns:
            raise AssertionError(f"{path.name} 欄位錯誤：{reader.fieldnames}")
        rows = list(reader)
    if len(rows) != expected_rows:
        raise AssertionError(
            f"{path.name} 列數錯誤：預期 {expected_rows}，實際 {len(rows)}。"
        )
    return rows


def validate_result_rows(rows: list[dict[str, str]]) -> None:
    if [row["race_group"] for row in rows] != [label for label, _ in GROUPS]:
        raise AssertionError("結果 CSV 必須依序只有高比例與低比例兩列。")
    numeric_columns = (
        "sample_size_before_cleaning",
        "sample_size_after_cleaning",
        "estimated_households",
        "Q1",
        "Median",
        "Q3",
        "IQR",
    )
    for row in rows:
        values = {column: Decimal(row[column]) for column in numeric_columns}
        if any(not value.is_finite() for value in values.values()):
            raise AssertionError("結果 CSV 含非有限數值。")
        if not values["Q1"] <= values["Median"] <= values["Q3"]:
            raise AssertionError(f"{row['race_group']} 四分位數順序錯誤。")
        if values["IQR"] != values["Q3"] - values["Q1"]:
            raise AssertionError(f"{row['race_group']} 的 IQR 不正確。")


def validate_quality_rows(rows: list[dict[str, str]]) -> None:
    for row in rows:
        before = int(row["sample_size_before_cleaning"])
        after = int(row["sample_size_after_cleaning"])
        excluded = int(row["total_excluded"])
        reason_total = sum(int(row[column]) for column in EXCLUSION_COLUMNS)
        weight = Decimal(row["total_weight_after_cleaning"])
        if before - after != excluded or excluded != reason_total:
            raise AssertionError(f"{row['state']} 品質報告排除總數不一致。")
        if not weight.is_finite() or weight <= 0:
            raise AssertionError(f"{row['state']} 清理後權重無效。")


def main() -> None:
    validate_source_files()
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    state_results: dict[str, StateResult] = {}
    for source in SOURCES:
        result = process_source(source)
        state_results[source.abbreviation] = result
        print(
            f"[{source.name}] 最終清理後樣本數：{len(result.records):,}；"
            f"清理後 WGTP 總和：{result.total_weight:,}"
        )

    result_rows = [
        calculate_group(label, abbreviations, state_results)
        for label, abbreviations in GROUPS
    ]
    quality_rows = build_quality_rows(state_results)

    validate_result_rows(result_rows)
    validate_quality_rows(quality_rows)
    write_csv_atomically(RESULTS_PATH, RESULT_COLUMNS, result_rows)
    write_csv_atomically(QUALITY_PATH, QUALITY_COLUMNS, quality_rows)

    saved_results = read_and_validate_csv(RESULTS_PATH, RESULT_COLUMNS, 2)
    validate_result_rows(saved_results)
    saved_quality = read_and_validate_csv(
        QUALITY_PATH, QUALITY_COLUMNS, expected_rows=len(SOURCES)
    )
    validate_quality_rows(saved_quality)
    if [row["state_fips"] for row in saved_quality] != [
        source.fips for source in SOURCES
    ]:
        raise AssertionError("品質報告州別順序或 FIPS 不正確。")

    print("\nCSV 重新讀取驗證通過：")
    print(f"  主要結果：2 列（{', '.join(row['race_group'] for row in saved_results)}）")
    print(f"  品質報告：{len(saved_quality)} 列")
    print(f"  主要結果檔已建立：{RESULTS_PATH}")
    print(f"  品質報告檔已建立：{QUALITY_PATH}")


if __name__ == "__main__":
    main()
