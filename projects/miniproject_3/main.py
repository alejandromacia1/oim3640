
import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

def get_latitude_longitude(place_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place_name}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    }

    data = requests.get(url, params=params).json()
    if not data["features"]:
        return None, None

    coords = data["features"][0]["geometry"]["coordinates"]
    return coords[1], coords[0]

def get_nearest_station(latitude, longitude):
    params = {
        "api_key": MBTA_API_KEY,
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "page[limit]": 1
    }