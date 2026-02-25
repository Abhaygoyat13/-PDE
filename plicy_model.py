import json

POLICY = {
    "allowed_domains": [
        "EdTech",
        "HealthTech",
        "FinTech",
        "AgriTech"
    ],

    "blocked_domains": [
        "Military",
        "Weapons",
        "Political Campaigning"
    ],

    "allowed_actions": ["discover_problems", "rank_problems"],
    "max_depth": "medium",
    "max_problems": 10,
    "risk_threshold": 0.6,

    "delegation": {
        "ranking_agent": {
            "can": ["rank_problems"],
            "cannot": ["discover_problems"],
            "max_input": 10
        }
    }
}
