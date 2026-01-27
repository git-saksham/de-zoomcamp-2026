# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 16:23:26 2026

@author: harik
"""

import pandas as pd

# URLs for the data
green_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'
zones_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

print("Processing data inside Docker...")
df = pd.read_parquet(green_url)
zones = pd.read_csv(zones_url)

# Q3
q3 = df[(df.trip_distance <= 1)].shape[0]
print(f"Q3: {q3}")

# Q4
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
q4 = df[df.trip_distance < 100].groupby(df.lpep_pickup_datetime.dt.date).trip_distance.max().idxmax()
print(f"Q4: {q4}")

# Q5
df_18 = df[df.lpep_pickup_datetime.dt.date == pd.to_datetime('2025-11-18').date()]
merged_18 = pd.merge(df_18, zones, left_on='PULocationID', right_on='LocationID')
q5 = merged_18.groupby('Zone').total_amount.sum().idxmax()
print(f"Q5: {q5}")

# Q6
df_zones = pd.merge(df, zones, left_on='PULocationID', right_on='LocationID')
ehn = df_zones[df_zones['Zone'] == 'East Harlem North']
ehn_final = pd.merge(ehn, zones, left_on='DOLocationID', right_on='LocationID', suffixes=('_pu', '_do'))
q6 = ehn_final.groupby('Zone_do').tip_amount.max().idxmax()
print(f"Q6: {q6}")