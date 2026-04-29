import os
import requests
from dotenv import load_dotenv

# Load environment variables
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
    return coords[1], coords[0]  # (lat, lon)


def get_nearest_station(latitude, longitude):
    params = {
        "api_key": MBTA_API_KEY,
        "filter[latitude]": latitude,
        "filter[longitude]": longitude,
        "sort": "distance",
        "page[limit]": 1
    }

    data = requests.get("https://api-v3.mbta.com/stops", params=params).json()

    if not data["data"]:
        return None, None

    stop = data["data"][0]["attributes"]

    # Correct field name from MBTA API
    wheelchair = stop.get("wheelchair_boarding")

    if wheelchair == 1:
        wheelchair_status = "Accessible"
    elif wheelchair == 2:
        wheelchair_status = "Inaccessible"
    else:
        wheelchair_status = "Unknown"

    return stop["name"], wheelchair_status

def find_stop_near(place_name):
    lat, lng = get_latitude_longitude(place_name)

    if lat is None:
        return None, None

    return get_nearest_station(lat, lng)

if __name__ == "__main__":
    for place in ["Boston Common", "Fenway Park"]:
        station, wheelchair_status = find_stop_near(place)
        print(f"{place} → {station} (Accessible: {wheelchair_status})")