"""Append Hawaii and Vermont income quartiles to the existing results CSV."""

from __future__ import annotations

import csv
import os
import tempfile
from pathlib import Path

from calculate_income_quartiles import process_state


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "income_quartiles_2024.csv"
REQUIRED_OUTPUT_COLUMNS = (
    "state",
    "state_fips",
    "sample_size_before_cleaning",
    "sample_size_after_cleaning",
    "estimated_households",
    "Q1",
    "Median",
    "Q3",
    "IQR",
)
STATE_FILES = (
    ("HI", 15, PROJECT_ROOT / "data" / "raw" / "csv_hhi" / "psam_h15.csv"),
    ("VT", 50, PROJECT_ROOT / "data" / "raw" / "csv_hvt" / "psam_h50.csv"),
)


def main() -> None:
    if not OUTPUT_PATH.is_file():
        raise FileNotFoundError(
            f"既有結果 CSV 不存在，為避免覆蓋或另建檔案，停止處理：{OUTPUT_PATH}"
        )

    results = [process_state(state, fips, path) for state, fips, path in STATE_FILES]

    with OUTPUT_PATH.open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        fieldnames = reader.fieldnames
        if fieldnames is None or not set(REQUIRED_OUTPUT_COLUMNS).issubset(fieldnames):
            raise ValueError(f"既有 CSV 欄位不符合需求：{fieldnames}")
        existing_rows = list(reader)

    existing_states = [row["state"] for row in existing_rows]
    if len(existing_states) != len(set(existing_states)):
        raise ValueError(f"既有 CSV 的州別重複，拒絕更新：{existing_states}")

    result_by_state = {str(result["state"]): result for result in results}
    updated_rows: list[dict[str, str]] = []
    seen_targets: set[str] = set()
    for old_row in existing_rows:
        state = old_row["state"]
        if state in result_by_state:
            result = result_by_state[state]
            updated_rows.append(
                {column: str(result[column]) if column in result else "" for column in fieldnames}
            )
            seen_targets.add(state)
        else:
            updated_rows.append(old_row)

    for state, _, _ in STATE_FILES:
        if state not in seen_targets:
            result = result_by_state[state]
            updated_rows.append(
                {column: str(result[column]) if column in result else "" for column in fieldnames}
            )

    fd, temporary_name = tempfile.mkstemp(
        prefix=f".{OUTPUT_PATH.name}.", suffix=".tmp", dir=OUTPUT_PATH.parent
    )
    try:
        with os.fdopen(fd, "w", newline="", encoding="utf-8") as destination:
            writer = csv.DictWriter(
                destination, fieldnames=fieldnames, lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(updated_rows)

        with Path(temporary_name).open("r", newline="", encoding="utf-8") as check:
            reader = csv.DictReader(check)
            verified_rows = list(reader)
            if reader.fieldnames != fieldnames:
                raise AssertionError("暫存 CSV 欄位順序與既有檔案不一致。")
            verified_by_state = {row["state"]: row for row in verified_rows}
            if len(verified_rows) != len(existing_rows) + sum(
                state not in existing_states for state, _, _ in STATE_FILES
            ):
                raise AssertionError("暫存 CSV 列數錯誤，既有資料可能遺失或新增列數不符。")

            for old_row in existing_rows:
                if old_row["state"] not in result_by_state:
                    if verified_by_state.get(old_row["state"]) != old_row:
                        raise AssertionError(
                            f"既有 {old_row['state']} 資料列在更新後發生變化。"
                        )

            for result in results:
                state = str(result["state"])
                row = verified_by_state.get(state)
                if row is None:
                    raise AssertionError(f"輸出缺少 {state} 資料列。")
                for column in REQUIRED_OUTPUT_COLUMNS:
                    if row[column] != str(result[column]):
                        raise AssertionError(
                            f"{state} 的 {column} 與本次計算結果不一致。"
                        )

        os.replace(temporary_name, OUTPUT_PATH)
    except Exception:
        if os.path.exists(temporary_name):
            os.unlink(temporary_name)
        raise

    with OUTPUT_PATH.open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        verified_rows = list(reader)
        if reader.fieldnames != fieldnames:
            raise AssertionError("輸出 CSV 欄位順序驗證失敗。")
    expected_states = existing_states.copy()
    for state, _, _ in STATE_FILES:
        if state not in expected_states:
            expected_states.append(state)
    if [row["state"] for row in verified_rows] != expected_states:
        raise AssertionError(
            f"輸出州別或順序錯誤：{[row['state'] for row in verified_rows]}"
        )

    print(f"\n輸出 CSV 已更新（保留既有列）：{OUTPUT_PATH}")
    print(
        f"重新讀取驗證：共 {len(verified_rows)} 列；"
        f"州別順序為 {', '.join(row['state'] for row in verified_rows)}；"
        f"新增／更新州別為 HI、VT；欄位順序與計算數值正確。"
    )


if __name__ == "__main__":
    main()
