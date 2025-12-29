# Ride Demand Heatmap Analyzer

## Overview
An interactive Python app that visualizes ride demand across different locations and hours using a heatmap. Users can filter by hour to see peak demand zones and spikes.

## Features
- Interactive heatmap of ride demand
- Filter by hour using sidebar
- Shows peak hour across all zones
- Displays raw data in a table

## Tech Stack
- Python
- NumPy
- Pandas
- Matplotlib / Seaborn
- Streamlit (for interactive web app)

## How to Run Locally

1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn streamlit
```
1. Run the application:
```bash
streamlit run app_interactive.py
```
## Dataset
ride_demand.csv is automatically generated if not present.
The dataset is synthetic and created for demonstration purposes.
Columns:
time – hour of the day
location – zone identifier
ride_requests – number of ride requests

## Future Improvements
- Add time slider for smoother hour selection
- Highlight peak zones dynamically
- Map-based visualization using latitude and longitude

## Skills Demonstrated
- Data cleaning and transformation
- Exploratory data analysis (EDA)
- Python application development
- Interactive dashboard creation


