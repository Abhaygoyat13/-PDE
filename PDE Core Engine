import json

def generate_problems(intent_dict):
    
    problems = []

    for i in range(intent_dict["max_problems"]):
        problems.append({
            "title": f"Unmet Need {i+1} in {intent_dict['domain']}",
            "description": "Sample problem description",
            "market_impact": 70 + i,
            "user_pain_index": 60 + i
        })

    return problems
