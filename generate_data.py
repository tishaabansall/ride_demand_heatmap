
import pandas as pd
import numpy as np

# Defining locations and hours
locations = ['Zone A', 'Zone B', 'Zone C', 'Zone D', 'Zone E']
hours = [f"{h:02d}:00" for h in range(24)]

# Generate fake ride requests data
data = []
for hour in hours:
    for loc in locations:
        rides = np.random.randint(5, 50)
        data.append([hour, loc, rides])

# Create dataframe 
df = pd.DataFrame(data, columns=['time', 'location', 'ride_requests'])
df.to_csv("data/ride_demand.csv", index=False)
print("Fake dataset created: ride_demand.csv")
