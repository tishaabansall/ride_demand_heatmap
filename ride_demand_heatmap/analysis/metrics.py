import pandas as pd

def peak_hour(df: pd.DataFrame):
    hourly = df.groupby("time")["ride_requests"].sum()
    return hourly.idxmax(), hourly.max()

def zone_ranking(df: pd.DataFrame):
    return (
        df.groupby("location")["ride_requests"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
