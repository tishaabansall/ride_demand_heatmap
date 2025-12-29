import os
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Ride Demand Heatmap", layout="wide")

DATA_FILE = "ride_demand.csv"

# generating synthetic data
# (real Uber data is not publicly available)

if not os.path.isfile(DATA_FILE):
    zones = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"]
    hours = [f"{h:02d}:00" for h in range(24)]

    rows = []
    for h in hours:
        for z in zones:
            rows.append([h, z, np.random.randint(5, 50)])

    df_gen = pd.DataFrame(rows, columns=["time", "location", "ride_requests"])
    df_gen.to_csv(DATA_FILE, index=False)
    st.info("Sample dataset created automatically.")

# loading data
df = pd.read_csv(DATA_FILE)

st.title("🚕 Ride Demand Heatmap Analyzer")
st.caption("Visualizing demand patterns across zones and time")

# sidebar
st.sidebar.header("Controls")
hour_choice = st.sidebar.selectbox(
    "Filter by hour",
    ["All"] + sorted(df["time"].unique().tolist())
)

if hour_choice != "All":
    df_view = df[df["time"] == hour_choice]
else:
    df_view = df

# prepare the heatmap data

heatmap_df = df_view.pivot(
    index="location",
    columns="time",
    values="ride_requests"
)

# plot
fig, ax = plt.subplots(figsize=(14, 6))
sns.heatmap(
    heatmap_df,
    cmap="YlOrRd",         ## to highlight high-demand spikes clearly

    linewidths=0.3,
    ax=ax
)


ax.set_xlabel("Time of Day")
ax.set_ylabel("Zone")

st.pyplot(fig)

# peak demand insight
hourly_total = df.groupby("time")["ride_requests"].sum()
peak_hour = hourly_total.idxmax()

st.markdown(
    f"**Peak demand hour:** `{peak_hour}`  \n"
    f"**Total rides:** `{hourly_total.max()}`"
)

# raw data
with st.expander("Show raw data"):
    st.dataframe(df_view, use_container_width=True)

# Limitation: data is aggregated hourly; finer-grained (e.g., 15-min) analysis
# could reveal more detailed demand spikes
