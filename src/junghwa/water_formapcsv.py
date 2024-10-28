import folium
from folium.plugins import MarkerCluster
import os
import webbrowser
import requests
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time
import pandas as pd
import numpy as np
import re

addresses_df = pd.read_csv('filtered_output.csv')

def simplify_address(address):
    """Simplifies a Korean address using re.search and additional condition."""
    # Convert address to string to ensure re.search works correctly
    address = str(address)
    match = re.search(r'(\w+동\d?가?)\s+(\d+)', address)  # Updated regex
    if match:
        return match.group(1) + ' ' + match.group(2)
    else:
        return address  # Return original address if no match

# Load filtered_output.csv with header
filtered_df = pd.read_csv('filtered_output.csv', encoding='utf-8-sig')

# Simplify the '지번주소' column in filtered_df
filtered_df['지번주소'] = filtered_df['지번주소'].apply(simplify_address)

def get_lat_lon(address):
    geolocator = Nominatim(user_agent="my_agent")
    retries = 3  # Number of retries
    delay = 2  # Delay in seconds between retries
    for i in range(retries):
        try:
            location = geolocator.geocode(address)
            if location:
                latitude = location.latitude
                longitude = location.longitude
                return latitude, longitude
            else:
                return np.nan, np.nan
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"Error geocoding '{address}': {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    print(f"Failed to geocode '{address}' after {retries} retries.")
    return np.nan, np.nan  # Return NaN if all retries fail

# Get latitude and longitude for each address
filtered_df[['latitude', 'longitude']] = filtered_df['지번주소'].apply(get_lat_lon).apply(pd.Series)
# Save filtered_df to csvformap.csv
filtered_df.to_csv('csvformap.csv', index=False, encoding='utf-8-sig')