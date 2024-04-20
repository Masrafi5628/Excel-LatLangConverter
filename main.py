import requests
import pandas as pd

def get_lat_lng(address):
    """
    Get latitude and longitude coordinates for a given address using Google Maps Geocoding API.
    """
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your Google Maps API key
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

# Read Excel file into pandas DataFrame
file_path = "your_excel_file.xlsx"  # Replace with the path to your Excel file
sheet_name = "Sheet2"  # Replace with the name of your sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Iterate over rows and get latitude and longitude for each address
latitudes = []
longitudes = []
for address in df['New Merge Value']:
    lat, lng = get_lat_lng(address)
    latitudes.append(lat)
    longitudes.append(lng)

# Add latitude and longitude columns to DataFrame
df['Latitude'] = latitudes
df['Longitude'] = longitudes

# Save DataFrame with latitude and longitude to a new Excel file
output_file_path = "output_with_lat_lng.xlsx"  # Replace with the desired output file path
df.to_excel(output_file_path, index=False)
