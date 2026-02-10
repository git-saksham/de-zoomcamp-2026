# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:27:39 2026

@author: harik
"""

import os
import urllib.request
from google.cloud import storage

# --- CONFIG ---
BUCKET_NAME = "YOUR_GCS_BUCKET_NAME"  # <--- CHANGE THIS
YEAR = "2024"
MONTHS = range(1, 7)  # Jan (1) to June (6)
# --------------

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def main():
    for month in MONTHS:
        month_str = f"{month:02d}"
        file_name = f"yellow_tripdata_{YEAR}-{month_str}.parquet"
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"
        
        print(f"Downloading {file_name}...")
        urllib.request.urlretrieve(url, file_name)
        
        print(f"Uploading {file_name} to GCS...")
        upload_to_gcs(BUCKET_NAME, file_name, file_name)
        
        # Clean up local file
        os.remove(file_name)

if __name__ == "__main__":
    main()