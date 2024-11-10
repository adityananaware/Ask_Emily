import json

with open("../data/rv_technician_data.json") as f:
    technician_data = json.load(f)

def find_technician(user_input):
    location = "extracted_location"
    nearby_technicians = [tech for tech in technician_data if tech["location"] == location]
    return nearby_technicians
