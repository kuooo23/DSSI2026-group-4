import pandas as pd

df = pd.read_csv("data/raw/ACSDT1Y2025_B02001-Data.csv", skiprows=[1])
df["white_pct"] = df["B02001_002E"] / df["B02001_001E"] * 100

out = df[["NAME", "B02001_001E", "B02001_002E", "white_pct"]]
out.to_csv("data/state_white_pct.csv", index=False)
print(out.sort_values("white_pct"))
