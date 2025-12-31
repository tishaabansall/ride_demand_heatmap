
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from analysis.metrics import peak_hour, zone_ranking


st.set_page_config(page_title="Ride Demand Heatmap", layout="wide")

DATA_FILE = "data/ride_demand.csv"

# loading data
df = pd.read_csv(DATA_FILE)

st.title(" Ride Demand Heatmap Analyzer")
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

# System-level insights


peak_h, peak_val = peak_hour(df)

st.markdown(f"""
###  System-Level Insights (All Hours)
- **Peak demand hour:** `{peak_h}`
- **Total rides at peak:** `{peak_val}`
""")

top_zones = zone_ranking(df).head(3)

st.markdown("###  Highest-demand zones(Throughout the Day)")
st.dataframe(top_zones, use_container_width=True)

# raw data
with st.expander("Show raw data"):
    st.dataframe(df_view, use_container_width=True)

# Limitation: data is aggregated hourly; finer-grained (e.g., 15-min) analysis
# could reveal more detailed demand spikes
