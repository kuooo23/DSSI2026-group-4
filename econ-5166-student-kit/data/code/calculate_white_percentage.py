"""Calculate the White-alone population percentage for U.S. states and D.C."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ACSDT1Y2024.B02001_2026-11-06T105406"
    / "Race data by state.csv"
)
OUTPUT_PATHS = (
    PROJECT_ROOT / "data" / "processed" / "white_percentage_by_state.csv",
    PROJECT_ROOT / "data" / "code" / "white_percentage_by_state.csv",
)
REQUIRED_COLUMNS = [
    "GEO_ID",
    "NAME",
    "B02001_001E",
    "B02001_002E",
]
OUTPUT_COLUMNS = [*REQUIRED_COLUMNS, "white_percentage"]
STATE_NAMES = {
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
}
DISTRICT_NAME = "District of Columbia"


def calculate_white_percentage() -> pd.DataFrame:
    """Read the ACS file, retain state-level records, and calculate percentages."""
    if not INPUT_PATH.is_file():
        raise FileNotFoundError(f"找不到原始 CSV 檔案：{INPUT_PATH}")

    # ACS downloads include a descriptive second row between the header and data.
    header = pd.read_csv(INPUT_PATH, nrows=0).columns
    missing_columns = set(REQUIRED_COLUMNS).difference(header)
    if missing_columns:
        raise ValueError(f"原始 CSV 缺少必要欄位：{sorted(missing_columns)}")

    data = pd.read_csv(
        INPUT_PATH,
        usecols=REQUIRED_COLUMNS,
        skiprows=[1],
        dtype={"GEO_ID": "string", "NAME": "string"},
    ).loc[:, REQUIRED_COLUMNS]

    # Convert Census estimates explicitly so non-numeric tokens cannot break math.
    for column in ("B02001_001E", "B02001_002E"):
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Match exact geography names to exclude national, territorial, and other rows.
    source_names = set(data["NAME"].dropna())
    keep_names = STATE_NAMES | (
        {DISTRICT_NAME} if DISTRICT_NAME in source_names else set()
    )
    result = data.loc[data["NAME"].isin(keep_names)].copy()

    if result["NAME"].duplicated().any():
        duplicates = sorted(
            result.loc[result["NAME"].duplicated(keep=False), "NAME"]
            .dropna()
            .unique()
            .tolist()
        )
        raise ValueError(f"原始 CSV 中州級地理資料重複：{duplicates}")

    expected_names = keep_names
    missing_geographies = expected_names.difference(set(result["NAME"].dropna()))
    if missing_geographies:
        raise ValueError(
            f"原始 CSV 缺少預期的州級資料：{sorted(missing_geographies)}"
        )

    # A missing or zero total population has no defined percentage.
    total_population = result["B02001_001E"]
    valid_denominator = total_population.notna() & total_population.ne(0)
    result["white_percentage"] = (
        result["B02001_002E"].div(total_population).mul(100).where(valid_denominator)
    ).round(2)

    return (
        result.loc[:, OUTPUT_COLUMNS]
        .sort_values("white_percentage", ascending=False, na_position="last")
        .reset_index(drop=True)
    )


def main() -> None:
    result = calculate_white_percentage()

    for output_path in OUTPUT_PATHS:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output_path, index=False)

    has_district = DISTRICT_NAME in set(result["NAME"])
    expected_count = 50 + int(has_district)
    all_expected_geographies_retained = (
        len(result) == expected_count
        and STATE_NAMES.issubset(set(result["NAME"]))
        and (not has_district or DISTRICT_NAME in set(result["NAME"]))
    )

    print(f"成功處理的州級資料數（含 D.C.）：{len(result)}")
    print(f"輸出檔案完整路徑：{OUTPUT_PATHS[0]}")
    print(f"另一份輸出檔案完整路徑：{OUTPUT_PATHS[1]}")
    print(f"是否保留所有預期的州級資料：{'是' if all_expected_geographies_retained else '否'}")

    ranked = result.dropna(subset=["white_percentage"])
    print("\n白人人口比例最高的前 5 個州級地區：")
    print(
        ranked.nlargest(5, "white_percentage")[
            ["NAME", "white_percentage"]
        ].to_string(index=False)
    )
    print("\n白人人口比例最低的前 5 個州級地區：")
    print(
        ranked.nsmallest(5, "white_percentage")[
            ["NAME", "white_percentage"]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as error:
        raise SystemExit(f"錯誤：{error}") from error
