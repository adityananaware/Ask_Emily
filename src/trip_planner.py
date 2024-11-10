import json

with open("../data/campground_data.json") as f:
    campground_data = json.load(f)

def plan_trip(user_input):
    recommendations = [camp for camp in campground_data if "Yellowstone" in user_input]
    return recommendations
