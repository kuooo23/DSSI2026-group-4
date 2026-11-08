"""Calculate weighted 2024 ACS PUMS income quartiles for two state groups."""

from __future__ import annotations

import csv
import hashlib
import os
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, localcontext
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = PROJECT_ROOT / "data" / "raw"
OUTPUT_ROOT = PROJECT_ROOT / "data" / "processed"
RESULTS_PATH = OUTPUT_ROOT / "income_quartiles_by_income_group_2024.csv"
QUALITY_PATH = OUTPUT_ROOT / "income_quartiles_data_quality_report_2024.csv"

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
        "MA",
        "Massachusetts",
        "25",
        RAW_ROOT / "csv_hma" / "psam_h25.csv",
        "f705f7384bd4fa2b9e16ea75987bea879ffc32ec2ae21dbe001fa74be1a39240",
    ),
    StateSource(
        "CO",
        "Colorado",
        "08",
        RAW_ROOT / "csv_hco" / "psam_h08.csv",
        "515b87c9c8d697afcc8d210821773c02b52672f3967fa24013df2faea8448b02",
    ),
    StateSource(
        "DC",
        "District of Columbia",
        "11",
        RAW_ROOT / "csv_hdc" / "psam_h11.csv",
        "9cf40696496ce3abad416ec02d1d839a97291c5ad3d442b52f20e48e4589ec42",
    ),
    StateSource(
        "NM",
        "New Mexico",
        "35",
        RAW_ROOT / "csv_hnm" / "psam_h35.csv",
        "b7ae2f4dcd639c78ed06952ec900f93a27d4e56b37ce4894eff7d7d73315c824",
    ),
    StateSource(
        "LA",
        "Louisiana",
        "22",
        RAW_ROOT / "csv_hla" / "psam_h22.csv",
        "d8367ac9ccab4ace8d49b36220a6577f035c0bea7fb133c2066f8157838c1642",
    ),
    StateSource(
        "MS",
        "Mississippi",
        "28",
        RAW_ROOT / "csv_hms" / "psam_h28.csv",
        "6086aaad1fd1e7c7a7b6889b470910f72ea140d911dc0ecb716929f817952243",
    ),
)
GROUPS = (
    ("High", ("MA", "CO", "DC")),
    ("Low", ("NM", "LA", "MS")),
)
SOURCE_BY_ABBREVIATION = {source.abbreviation: source for source in SOURCES}
REQUIRED_COLUMNS = {"STATE", "TYPEHUGQ", "HINCP", "WGTP", "ADJINC", "SERIALNO"}
RESULT_COLUMNS = (
    "income_group",
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
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_source_files() -> None:
    missing: list[str] = []
    for source in SOURCES:
        readme = source.path.parent / "ACS2024_PUMS_README.pdf"
        if not source.path.is_file():
            missing.append(str(source.path))
        if not readme.is_file():
            missing.append(str(readme))
    if missing:
        raise FileNotFoundError(
            "缺少必要的 2024 ACS PUMS 原始資料或 README，停止處理：\n"
            + "\n".join(missing)
        )

    expected_header: tuple[str, ...] | None = None
    for source in SOURCES:
        with source.path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            header = next(reader, None)
        if header is None:
            raise ValueError(f"{source.path} 是空檔。")
        if len(header) != len(set(header)):
            raise ValueError(f"{source.path} 有重複欄名：{header}")
        if expected_header is None:
            expected_header = tuple(header)
        elif tuple(header) != expected_header:
            raise ValueError(
                f"{source.path} 欄位名稱或順序與其他州資料不一致。"
            )
        missing_columns = REQUIRED_COLUMNS.difference(header)
        if missing_columns:
            raise ValueError(
                f"{source.path} 缺少必要欄位：{sorted(missing_columns)}"
            )

        actual_hash = sha256_file(source.path)
        if actual_hash != source.expected_sha256:
            raise ValueError(
                f"{source.path} 的 SHA-256 與已核對版本不符；"
                "為避免使用不同資料版本，停止處理。"
            )
    print(
        "六份原始 CSV 欄位名稱與順序一致；處理後欄位型態統一為 "
        "STATE 字串及數值 Decimal。"
    )
    print(
        f"2024 PUMS 字典：HINCP -60000 為 N/A；合法數值範圍 "
        f"{HINCP_MIN_VALID} 至 {HINCP_MAX_VALID}（包含合法負收入）；"
        f"來源：{DATA_DICTIONARY_URL}"
    )


def check_hincp_value(result: StateResult, raw_value: str | None) -> Decimal | None:
    value = "" if raw_value is None else raw_value.strip()
    if not value:
        result.raw_hincp_missing += 1
        return None

    parsed = parse_decimal(value)
    if parsed is None:
        result.unexpected_hincp_tokens[value] += 1
        return None
    if parsed == HINCP_NA_CODE:
        result.raw_hincp_special += 1
        return parsed
    if parsed != parsed.to_integral_value():
        result.fractional_hincp[value] += 1
        return parsed
    if parsed < HINCP_MIN_VALID or parsed > HINCP_MAX_VALID:
        result.out_of_range_hincp[value] += 1
        return parsed
    if parsed < 0:
        result.raw_hincp_negative += 1
    return parsed


def print_data_quality(result: StateResult) -> None:
    source = result.source
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
    if result.invalid_serial_numbers:
        print(f"  非 2024 SERIALNO 筆數：{result.invalid_serial_numbers:,}")
    if result.invalid_state_values:
        print(f"  不符合預期 FIPS 的 STATE 值：{dict(result.invalid_state_values)}")
    if result.unexpected_hincp_tokens:
        print(f"  未知 HINCP 代碼（未自行刪除）：{dict(result.unexpected_hincp_tokens)}")
    if result.out_of_range_hincp:
        print(f"  超出字典範圍的 HINCP（未自行刪除）：{dict(result.out_of_range_hincp)}")
    if result.fractional_hincp:
        print(f"  非整數 HINCP（未自行刪除）：{dict(result.fractional_hincp)}")


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

            serial_number = (row.get("SERIALNO") or "").strip()
            if not serial_number.startswith("2024"):
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

            income = check_hincp_value(result, row.get("HINCP"))

            adjustment_text = row.get("ADJINC")
            adjustment = parse_decimal(adjustment_text)
            adjustment_value = (
                "" if adjustment_text is None else adjustment_text.strip()
            )
            if not adjustment_value:
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
            if not (row.get("HINCP") or "").strip():
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

    print_data_quality(result)
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
            f"[{source.abbreviation}] HINCP 含資料字典未定義或不符合型態的值；"
            "已列出而未自行推定或排除。"
        )

    exclusions = {
        column: result.exclusions[column] for column in EXCLUSION_COLUMNS
    }
    excluded_total = sum(exclusions.values())
    if excluded_total + len(result.records) != result.sample_size_before_cleaning:
        raise AssertionError(
            f"[{source.abbreviation}] 逐步清理筆數不守恆："
            f"清理前={result.sample_size_before_cleaning}，"
            f"清理後={len(result.records)}，排除={excluded_total}。"
        )
    if not result.records:
        raise ValueError(f"[{source.abbreviation}] 清理後沒有可用的家庭紀錄。")

    print("  逐步排除筆數（原因互斥）：")
    for column in EXCLUSION_COLUMNS:
        print(f"    {column}: {exclusions[column]:,}")
    print(f"  清理後筆數：{len(result.records):,}")
    print(f"  清理後 WGTP 總和：{result.total_weight:,}")
    return result


def weighted_empirical_quantile(
    records: Iterable[CleanRecord], quantile: Decimal
) -> Decimal:
    if quantile <= 0 or quantile > 1:
        raise ValueError(f"分位數比例必須介於 (0, 1]：{quantile}")

    weights_by_income: defaultdict[Decimal, Decimal] = defaultdict(Decimal)
    for record in records:
        if record.wgtp <= 0 or not record.wgtp.is_finite():
            raise ValueError("加權分位數輸入含非正數或無效 WGTP。")
        weights_by_income[record.adjusted_income] += record.wgtp

    total_weight = sum(weights_by_income.values(), Decimal(0))
    if total_weight <= 0:
        raise ValueError("加權分位數的總權重必須大於 0。")

    threshold = total_weight * quantile
    cumulative_weight = Decimal(0)
    for income in sorted(weights_by_income):
        cumulative_weight += weights_by_income[income]
        if cumulative_weight >= threshold:
            return income
    raise AssertionError("累積權重未達到分位數門檻。")


def format_decimal(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def calculate_group(
    label: str, abbreviations: tuple[str, ...], results: dict[str, StateResult]
) -> dict[str, str]:
    records = [
        record
        for abbreviation in abbreviations
        for record in results[abbreviation].records
    ]
    if not records:
        raise ValueError(f"{label} 組清理後沒有有效家庭資料。")

    fields = {
        name: weighted_empirical_quantile(records, proportion)
        for name, proportion in QUANTILES
    }
    q1 = fields["Q1"]
    median = fields["Median"]
    q3 = fields["Q3"]
    iqr = q3 - q1
    if not q1 <= median <= q3:
        raise AssertionError(f"{label} 組四分位數順序錯誤：{fields}")
    if iqr != q3 - q1:
        raise AssertionError(f"{label} 組 IQR 與 Q3 - Q1 不一致。")

    before = sum(
        results[abbreviation].sample_size_before_cleaning
        for abbreviation in abbreviations
    )
    after = len(records)
    total_weight = sum((record.wgtp for record in records), Decimal(0))
    included_states = "; ".join(
        SOURCE_BY_ABBREVIATION[abbreviation].name
        for abbreviation in abbreviations
    )
    row = {
        "income_group": label,
        "included_states": included_states,
        "sample_size_before_cleaning": str(before),
        "sample_size_after_cleaning": str(after),
        "estimated_households": format_decimal(total_weight),
        "Q1": format_decimal(q1),
        "Median": format_decimal(median),
        "Q3": format_decimal(q3),
        "IQR": format_decimal(iqr),
    }

    expected_states = {
        SOURCE_BY_ABBREVIATION[abbreviation].fips
        for abbreviation in abbreviations
    }
    if {record.state for record in records} != expected_states:
        raise AssertionError(f"{label} 組合併後 STATE 欄位遺失或含非預期州碼。")

    print(f"\nGroup {label} 合併後樣本數：{after:,}")
    print(f"Group {label} 清理前樣本數：{before:,}")
    print(f"Group {label} WGTP 權重總和：{total_weight:,}")
    print(
        f"Group {label} 加權四分位數（Weighted Empirical Quantile）："
        f"Q1={q1}；Median={median}；Q3={q3}；IQR={iqr}"
    )
    print(f"Group {label} 驗證 Q1 <= Median <= Q3：通過")
    print(f"Group {label} 驗證 IQR = Q3 - Q1：通過")
    print(f"Group {label} 加權方法驗證：所有收入依序累加 WGTP，重複收入先合併權重")
    return row


def build_quality_rows(results: dict[str, StateResult]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in SOURCES:
        result = results[source.abbreviation]
        counts = {
            column: result.exclusions[column] for column in EXCLUSION_COLUMNS
        }
        total_excluded = sum(counts.values())
        if total_excluded + len(result.records) != result.sample_size_before_cleaning:
            raise AssertionError(f"[{source.abbreviation}] 品質報告排除總數錯誤。")
        rows.append(
            {
                "state": source.name,
                "state_fips": source.fips,
                "sample_size_before_cleaning": str(result.sample_size_before_cleaning),
                "sample_size_after_cleaning": str(len(result.records)),
                **{column: str(counts[column]) for column in EXCLUSION_COLUMNS},
                "total_excluded": str(total_excluded),
                "total_weight_after_cleaning": format_decimal(result.total_weight),
            }
        )
    return rows


def write_temp_csv(
    path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]
) -> Path:
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        newline="",
        encoding="utf-8",
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=path.parent,
        delete=False,
    )
    temporary_path = Path(handle.name)
    try:
        with handle:
            writer = csv.DictWriter(
                handle, fieldnames=columns, lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(rows)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise
    return temporary_path


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


def validate_results_csv(rows: list[dict[str, str]]) -> None:
    if [row["income_group"] for row in rows] != ["High", "Low"]:
        raise AssertionError("主要結果 CSV 必須依序只有 High、Low 兩列。")
    numeric_fields = (
        "sample_size_before_cleaning",
        "sample_size_after_cleaning",
        "estimated_households",
        "Q1",
        "Median",
        "Q3",
        "IQR",
    )
    for row in rows:
        numbers = {field: Decimal(row[field]) for field in numeric_fields}
        if any(not value.is_finite() for value in numbers.values()):
            raise AssertionError("主要結果 CSV 含非有限數值。")
        if not (
            numbers["Q1"] <= numbers["Median"] <= numbers["Q3"]
        ):
            raise AssertionError(f"{row['income_group']} 組四分位數順序錯誤。")
        if numbers["IQR"] != numbers["Q3"] - numbers["Q1"]:
            raise AssertionError(f"{row['income_group']} 組 IQR 計算錯誤。")
        if numbers["sample_size_after_cleaning"] <= 0:
            raise AssertionError(f"{row['income_group']} 組清理後樣本數無效。")
        if numbers["estimated_households"] <= 0:
            raise AssertionError(f"{row['income_group']} 組總權重無效。")


def validate_quality_rows(rows: list[dict[str, str]]) -> None:
    for row in rows:
        before = int(row["sample_size_before_cleaning"])
        after = int(row["sample_size_after_cleaning"])
        excluded = int(row["total_excluded"])
        reason_total = sum(int(row[column]) for column in EXCLUSION_COLUMNS)
        weight = Decimal(row["total_weight_after_cleaning"])
        if before - after != excluded or excluded != reason_total:
            raise AssertionError(f"{row['state']} 品質報告的逐步排除數不一致。")
        if not weight.is_finite() or weight <= 0:
            raise AssertionError(f"{row['state']} 品質報告的清理後權重無效。")


def main() -> None:
    validate_source_files()
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    results: dict[str, StateResult] = {}
    for source in SOURCES:
        results[source.abbreviation] = process_source(source)

    result_rows = [
        calculate_group(label, abbreviations, results)
        for label, abbreviations in GROUPS
    ]
    quality_rows = build_quality_rows(results)

    result_temporary = write_temp_csv(RESULTS_PATH, RESULT_COLUMNS, result_rows)
    quality_temporary = write_temp_csv(QUALITY_PATH, QUALITY_COLUMNS, quality_rows)
    try:
        temporary_results = read_and_validate_csv(
            result_temporary, RESULT_COLUMNS, expected_rows=2
        )
        validate_results_csv(temporary_results)
        temporary_quality = read_and_validate_csv(
            quality_temporary, QUALITY_COLUMNS, expected_rows=len(SOURCES)
        )
        validate_quality_rows(temporary_quality)

        os.replace(result_temporary, RESULTS_PATH)
        os.replace(quality_temporary, QUALITY_PATH)
    finally:
        result_temporary.unlink(missing_ok=True)
        quality_temporary.unlink(missing_ok=True)

    saved_results = read_and_validate_csv(RESULTS_PATH, RESULT_COLUMNS, 2)
    validate_results_csv(saved_results)
    saved_quality = read_and_validate_csv(
        QUALITY_PATH, QUALITY_COLUMNS, expected_rows=len(SOURCES)
    )
    validate_quality_rows(saved_quality)
    if [row["state_fips"] for row in saved_quality] != [
        source.fips for source in SOURCES
    ]:
        raise AssertionError("品質報告的州別或順序錯誤。")

    print("\n已使用兩組各自合併後的樣本，以 WGTP 加權計算分位數。")
    print("最終主要 CSV 重新讀取驗證：2 列（High、Low）、欄位及數值正確。")
    print(f"主要結果 CSV 已建立：{RESULTS_PATH}")
    print(f"資料品質報告已建立：{QUALITY_PATH}")


if __name__ == "__main__":
    main()
