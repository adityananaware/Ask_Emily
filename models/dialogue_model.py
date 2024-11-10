import spacy

nlp = spacy.load("en_core_web_md")

def analyze_intent(user_input):
    doc = nlp(user_input)
    if "trip" in doc.text:
        return "trip_planning"
    elif "technician" in doc.text:
        return "technician_finder"
    elif "route" in doc.text:
        return "gps_navigation"
    else:
        return "general_inquiry"
