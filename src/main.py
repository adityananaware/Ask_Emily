from trip_planner import plan_trip
from gps_module import get_route
from technician_finder import find_technician
from models.dialogue_model import analyze_intent

def main(user_input):
    intent = analyze_intent(user_input)

    if intent == "trip_planning":
        return plan_trip(user_input)
    elif intent == "gps_navigation":
        return get_route(user_input)
    elif intent == "technician_finder":
        return find_technician(user_input)
    else:
        return "How can I assist you today with your travel plans?"
