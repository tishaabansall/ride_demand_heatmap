# Ride Demand Heatmap Analyzer

## Overview
An interactive Python app that visualizes ride demand across different locations and hours using a heatmap. Users can filter by hour to see peak demand zones and spikes.

## Features
- Interactive heatmap of ride demand
- Filter by hour using sidebar
- Shows peak hour across all zones
- Displays raw data in a table
- Beginner-friendly and fully functional

## Tech Stack
- Python
- Pandas
- Matplotlib / Seaborn
- Streamlit (for interactive web app)

## How to Run Locally
1. Install dependencies:
pip install pandas matplotlib seaborn streamlit
2. Run the app:
streamlit run app_interactive.py

## Dataset
- `ride_demand.csv` contains fake or real ride request data.
- Columns: `time`, `location`, `ride_requests`

## Future Improvements
- Add time slider for smoother hour selection
- Highlight peak zones dynamically
- Map-based visualization using latitude and longitude


