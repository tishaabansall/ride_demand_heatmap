# Ride Demand Heatmap Analyzer

## Overview
An interactive Streamlit-based analytics dashboard that visualizes ride demand across urban zones and hours.
The project helps identify peak demand hours, high-demand zones, and system-wide demand patterns to support data-driven driver allocation decisions.

This project demonstrates end-to-end data analysis: data loading, transformation, metric computation, and interactive visualization.

## Key Features
- **Hourly Demand Heatmap**  
  Visualizes ride requests across zones and time using a color-coded heatmap.
- **Time-Based Filtering**  
  Filter demand patterns by hour to analyze temporal spikes.
- **System-Level Insights**  
  Displays the global peak demand hour and total ride volume.
- **Zone Ranking**  
  Ranks zones based on total ride demand.
- **Raw Data Inspection**  
  View filtered or full datasets directly within the app.


## Tech Stack
- Python
- NumPy
- Pandas
- Matplotlib / Seaborn
- Streamlit (for interactive web app)

## Project Structure

```text
# Project Structure

ride_demand_heatmap/
├── analysis/
│   ├── __init__.py
│   └── metrics.py
├── data/
│   └── ride_demand.csv
├── screenshots/
│   ├── heatmap_overview.png
│   └── system_insights.png
├── scripts/
│   └── generate_data.py
├── app.py
```

## How to Run Locally

1. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn streamlit
```
1. Run the application:
```bash
streamlit run app_interactive.py
```

## Demo

### Ride Demand Heatmap
![Heatmap Overview](screenshots/heatmap_overview.png)

### System Insights
![System Insights](screenshots/system_insights.png)


## Dataset
- ride_demand.csv is automatically generated if not present.
- The dataset is synthetic and created for demonstration purposes.
- Columns:
   - time – hour of the day
   - location – zone identifier
   - ride_requests – number of ride requests


## Future Improvements
- Add time slider for smoother hour selection
- Highlight peak zones dynamically
- Map-based visualization using latitude and longitude

## Skills Demonstrated
- Data analysis and aggregation
- Exploratory data analysis (EDA)
- Metric design and interpretation
- Python project structuring
- Interactive dashboard development


