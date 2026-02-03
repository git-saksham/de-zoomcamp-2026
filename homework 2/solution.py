# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 09:47:15 2026

@author: harik
"""

import pandas as pd
import requests
# SOLUTION SCRIPT FOR HOMEWORK 2
# Calculates row counts and checks file sizes programmatically.

def get_row_count(color, year, months):
    total_rows = 0
    print(f"--- Processing {color} taxi data for {year} ---")
    
    for month in months:
        month_str = f"{month:02d}"
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{color}_tripdata_{year}-{month_str}.csv.gz"
        
        try:
            # Read only the first column for speed
            df = pd.read_csv(url, usecols=[0], low_memory=False)
            rows = len(df)
            total_rows += rows
            print(f"Month {month_str}: {rows:,} rows")
        except Exception as e:
            print(f"Error reading month {month_str}: {e}")
            
    print(f"TOTAL ROWS for {color} {year}: {total_rows:,}\n")
    response = requests.head(url)
    size_in_bytes = int(response.headers['Content-Length'])
    size_in_mib = size_in_bytes / (1024 * 1024)
    
    print(f"Size: {size_in_mib:.2f} MiB")
if __name__ == "__main__":
    # Q3: Yellow Taxi 2020
    get_row_count('yellow', 2020, range(1, 13))

    # Q4: Green Taxi 2020
    get_row_count('green', 2020, range(1, 13))

    # Q5: Yellow Taxi March 2021
    get_row_count('yellow', 2021, [3])