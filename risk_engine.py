import json

def calculate_risk(intent_dict):

    risk = 0.0
    domain_lower = intent_dict["domain"].lower()

    sensitive_keywords = ["military", "weapon", "political"]

    # Exact blocked match
    if intent_dict["domain"] in POLICY["blocked_domains"]:
        risk += 1.0

    # Keyword detection (prevents bypass)
    for word in sensitive_keywords:
        if word in domain_lower:
            risk += 0.4

    if intent_dict["depth_level"] == "high":
        risk += 0.3

    if intent_dict["max_problems"] > 8:
        risk += 0.2

    return min(risk, 1.0)
