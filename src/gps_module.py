import requests
import json

with open('../config/credentials.json') as f:
    credentials = json.load(f)

def get_route(user_input):
    destination = "Yellowstone"  # Placeholder for extracted location from user input
    response = requests.get(f"https://maps.googleapis.com/maps/api/directions/json?destination={destination}&key={credentials['google_maps_api_key']}")
    return response.json()
