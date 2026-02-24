import json

def ranking_agent(problems):
    
    delegation = POLICY["delegation"]["ranking_agent"]

    if len(problems) > delegation["max_input"]:
        return "Blocked: Too many problems for ranking agent"

    ranked = sorted(problems, key=lambda x: x["market_impact"], reverse=True)

    return ranked
