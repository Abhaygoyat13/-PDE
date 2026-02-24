import json

def validate_intent(intent_dict):
    
    domain = intent_dict["domain"]

    # Hard block exact match
    if domain in POLICY["blocked_domains"]:
        return False, "Blocked Domain"

    # Block keyword-based variations
    for blocked in POLICY["blocked_domains"]:
        if blocked.lower() in domain.lower():
            return False, "Blocked Domain (Keyword Match)"

    # Allow only approved domains
    if domain not in POLICY["allowed_domains"]:
        return False, "Domain Not Allowed"

    if intent_dict["action"] not in POLICY["allowed_actions"]:
        return False, "Action Not Allowed"

    if intent_dict["depth_level"] != POLICY["max_depth"]:
        return False, "Depth Level Exceeded"

    if intent_dict["max_problems"] > POLICY["max_problems"]:
        return False, "Problem Limit Exceeded"

    risk = calculate_risk(intent_dict)

    if risk > POLICY["risk_threshold"]:
        return False, f"Risk Too High: {risk}"

    return True, "Allowed"
