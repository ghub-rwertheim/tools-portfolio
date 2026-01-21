import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

# --- CONFIGURATION ---
props = "test.props"
group_id = "12345"  # account users
target_user = "71414961809622"  # The id to search for

# ---------------------

properties_path = Path(__file__).parent / "props" / props
script_dir = Path(__file__).parent.resolve()
load_dotenv(properties_path)

if not properties_path.is_file():
    print(f"ERROR: The properties file was NOT found at {properties_path}")
else:
    load_dotenv(dotenv_path=properties_path)

url = os.getenv("URL")
token = os.getenv("TOKEN")
scim_url = f"{url.rstrip('/')}/Groups/{group_id}"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/scim+json"
}

try:
    response = requests.get(scim_url, headers=headers)
    response.raise_for_status()
    group_data = response.json()

    if group_data:
        print(f"Group Name: {group_data.get('displayName')}")

        # Get the members list (defaults to empty list if no members found)
        members = group_data.get('members', [])

        print("\n")
        pretty_json = json.dumps(group_data, indent=4)
        print(pretty_json)

        # Search for the user
        found_user = next((m for m in members if m.get('value').lower() == target_user.lower()), None)

        if found_user:
            print(f"USER FOUND: {target_user}")
            print(json.dumps(found_user, indent=2))
        else:
            print(f"USER NOT FOUND: {target_user}")
            # Print all members to see what's available
            # print(f"Available members: {[m.get('display') for m in members]}")

except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
