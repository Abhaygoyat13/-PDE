import json

def log_event(intent_dict, decision, message, risk):
    
    log = {
        "intent": intent_dict,
        "decision": decision,
        "message": message,
        "risk_score": risk
    }

    print(json.dumps(log, indent=4))
