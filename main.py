import json

def main():

    intent = Intent(
        action="discover_problems",
        domain="EdTech",
        depth_level="medium",
        max_problems=5
    )

    intent_dict = intent.to_dict()

    risk = calculate_risk(intent_dict)
    allowed, message = validate_intent(intent_dict)

    log_event(intent_dict, allowed, message, risk)

    if not allowed:
        print("Execution Blocked.")
        return

    problems = generate_problems(intent_dict)

    ranked = ranking_agent(problems)

    print(json.dumps(ranked, indent=4))


if _name_ == "_main_":
    main()
