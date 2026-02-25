import os
import json
from flask import Flask, jsonify, request
from dotenv import load_dotenv


from intent_model import Intent
from risk_engine import calculate_risk
from validator import validate_intent
from logger import log_event
from ranking_agent import ranking_agent

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():

    return jsonify({"status": "live", "agent": "Problem Discovery Engine"}), 200

@app.route('/discover', methods=['POST'])
def discover():

    data = request.json
    
    intent = Intent(
        action=data.get("action", "discover_problems"),
        domain=data.get("domain", "EdTech"),
        depth_level=data.get("depth_level", "medium"),
        max_problems=data.get("max_problems", 5)
    )

    intent_dict = intent.to_dict()
    risk = calculate_risk(intent_dict)
    allowed, message = validate_intent(intent_dict)
    
    log_event(intent_dict, allowed, message, risk)

    if not allowed:
        return jsonify({"error": "Execution Blocked", "reason": message}), 403

    from core_engine import generate_problems 
    problems = generate_problems(intent_dict)
    ranked = ranking_agent(problems)

    return jsonify(ranked)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
