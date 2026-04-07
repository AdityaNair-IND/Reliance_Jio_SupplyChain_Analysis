import marimo

__generated_with = "0.22.0"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fixing our dataset to have Indian warehouses and distribution centres.
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    import numpy as np

    return np, pd


@app.cell
def _():
    INPUT_FILE = "reliance_jio_supply_chain_500k.xlsx"
    OUTPUT_FILE = "jio_supply_chain.xlsx"
    SHEET_NAME = "Lifecycle_Events_500K"  
    return INPUT_FILE, OUTPUT_FILE, SHEET_NAME


@app.cell
def _(INPUT_FILE, SHEET_NAME, np, pd):
    np.random.seed(42)

    df_raw = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)

    df_indianized = df_raw.copy()

    original_row_count = df_indianized.shape[0]
    return df_indianized, original_row_count


@app.cell
def _():
    warehouse_mapping = {
        "WH_CENTRAL_TX": ["WH_NORTH_DL", "DC_NORTH_UP", "WH_NORTH_CH", "DC_CENTRAL_MP"],
        "WH_WEST_CA": ["WH_WEST_MH", "DC_CENTRAL_MH", "WH_WEST_GJ", "DC_WEST_RJ"],
        "WH_EAST_PA": ["WH_EAST_WB", "DC_EAST_JH", "DC_EAST_OD", "WH_NORTHEAST_AS"],
        "WH_SOUTH_GA": ["WH_SOUTH_KA", "DC_SOUTH_TN", "DC_SOUTH_TG", "DC_SOUTH_KL"]
    }
    return (warehouse_mapping,)


@app.cell
def _(df_indianized, np, warehouse_mapping):
    def map_warehouse_series(series):
        mapped = series.copy()

        for old_wh, new_list in warehouse_mapping.items():
            mask = series == old_wh
            n = mask.sum()

            if n > 0:
                mapped.loc[mask] = np.random.choice(new_list, size=n)

        return mapped

    df_indianized["warehouse_id"] = map_warehouse_series(df_indianized["warehouse_id"])
    return


@app.cell
def _(df_indianized):
    df_indianized["state_code"] = df_indianized["warehouse_id"].str.split("_").str[-1]

    df_indianized["facility_type"] = df_indianized["warehouse_id"].str.split("_").str[0]

    region_map = {
        "DL": "North", "UP": "North", "CH": "North",
        "MP": "Central",
        "MH": "West", "GJ": "West", "RJ": "West",
        "WB": "East", "JH": "East", "OD": "East",
        "AS": "Northeast",
        "KA": "South", "TN": "South", "TG": "South", "KL": "South"
    }

    df_indianized["region"] = df_indianized["state_code"].map(region_map)

    if "warehouse_region" in df_indianized.columns:
        df_indianized["warehouse_region"] = df_indianized["region"]
    return


@app.cell
def _(df_indianized, original_row_count, warehouse_mapping):
    assert df_indianized.shape[0] == original_row_count, "Row count mismatch!"

    legacy_values = set(warehouse_mapping.keys())
    assert not df_indianized["warehouse_id"].isin(legacy_values).any(), "Legacy warehouse IDs still exist!"

    assert df_indianized["region"].isnull().sum() == 0, "Null regions found!"
    assert df_indianized["state_code"].isnull().sum() == 0, "Null state codes found!"
    return


@app.cell
def _(OUTPUT_FILE, df_indianized):
    df_indianized.to_excel(OUTPUT_FILE, index=False)
    return


@app.cell
def _(df_indianized):
    print(df_indianized["warehouse_id"].value_counts())
    return


@app.cell
def _(df_indianized):
    print(df_indianized["warehouse_id"].nunique())
    return


@app.cell
def _(df_indianized):
    print(df_indianized["region"].value_counts())
    return


@app.cell
def _(df_indianized):
    print(df_indianized["facility_type"].value_counts())
    return


@app.cell
def _(df_indianized):
    df = df_indianized.copy()
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Cleaning + Optimization + Light EDA
    """)
    return


@app.cell
def _(df, pd):
    df["event_ts"] = pd.to_datetime(df["event_ts"], errors="coerce")
    return


@app.cell
def _(df):
    assert df["event_ts"].isnull().sum() == 0, "Invalid timestamps detected"
    return


@app.cell
def _(df):
    for col in ["on_time_flag", "anomaly_flag", "revenue_leakage_flag"]:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype("int8")
    return


@app.cell
def _(df):
    df["delay_days"] = df["delay_days"].fillna(0)
    df["actual_cycle_days"] = df["actual_cycle_days"].fillna(0)
    df["inventory_delta"] = df["inventory_delta"].fillna(0)
    return


@app.cell
def _(df):
    null_summary = df.isnull().sum().sort_values(ascending=False)
    print(null_summary)
    return (null_summary,)


@app.cell
def _(null_summary):
    null_columns = null_summary[null_summary > 0]
    print("\nColumns with nulls:\n", null_columns)
    return


@app.cell
def _(df):
    null_percent = (df.isnull().mean() * 100).sort_values(ascending=False)
    print("\nNull %:\n", null_percent[null_percent > 0])
    return


@app.cell
def _(df):
    total_memory_mb = df.memory_usage(deep=True).sum() / 1e6
    print(f"\nTotal Memory Usage: {total_memory_mb:.2f} MB")
    return


@app.cell
def _(df):
    memory_per_col = (df.memory_usage(deep=True) / 1e6).sort_values(ascending=False)
    print("\nMemory Usage by Column (MB):\n", memory_per_col)
    return


@app.cell
def _(df):
    print("\nShape:", df.shape)
    print("\nDtypes:\n", df.dtypes.value_counts())
    return


@app.cell
def _(df):
    for _col in df.select_dtypes(include="string").columns:
        df[_col] = df[_col].astype("category")
    return


@app.cell
def _(df):
    df["facility_type"] = df["facility_type"].astype("category")
    df["state_code"] = df["state_code"].astype("category")
    df["region"] = df["region"].astype("category")
    return


@app.cell
def _(df, pd):
    for _col in df.select_dtypes(include=["int64"]).columns:
        df[_col] = pd.to_numeric(df[_col], downcast="integer")

    for _col in df.select_dtypes(include=["float64"]).columns:
        df[_col] = pd.to_numeric(df[_col], downcast="float")
    return


@app.cell
def _(df):
    print(df.memory_usage(deep=True).sum() / 1e6)
    return


@app.cell
def _(df):
    print(df.dtypes.value_counts())
    return


@app.cell
def _(df):
    print(df.dtypes.apply(lambda x: str(x)).value_counts())
    return


@app.cell
def _(df):
    print("Duplicate rows:", df.duplicated().sum())
    return


@app.cell
def _(df):
    print("Unique event_id:", df["event_id"].nunique())
    print("Total rows:", len(df))
    return


@app.cell
def _(df):
    print(df["qty"].describe())
    print(df["sell_price"].describe())
    print(df["delay_days"].describe())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
