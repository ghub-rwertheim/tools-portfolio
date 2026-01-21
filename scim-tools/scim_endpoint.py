import json
from flask import Flask, request, jsonify

app = Flask(__name__)


# Catch everything: /Users, /Users/123, etc.
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def catch_scim_flow(path):
    print(f"\n{'=' * 20} {request.method} /{path} {'=' * 20}")

    # 1. Log Headers (to see if it's a PATCH or POST)
    print(f"Content-Type: {request.headers.get('Content-Type')}")

    # 2. Log Body (force=True to catch PATCH operations)
    payload = request.get_json(force=True, silent=True)
    if payload:
        print("--- RECEIVED PAYLOAD ---")
        print(json.dumps(payload, indent=4))
    else:
        print("No JSON body found.")

    # 3. CRITICAL: For POST requests, you MUST return a dummy 'id'
    # so the client knows who to send the subsequent PATCH requests to.
    if request.method == 'POST':
        # Use a consistent dummy ID for testing
        dummy_id = "71891328068620"
        return jsonify({
            "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
            "id": dummy_id,
            "userName": payload.get("userName", "unknown") if payload else "unknown",
            "meta": {"resourceType": "User", "location": f"/Users/{dummy_id}"}
        }), 201

    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)