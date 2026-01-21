import os
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

props = "test.props"

user_id = "12345"


properties_path = Path(__file__).parent / "props" / props
script_dir = Path(__file__).parent.resolve()
load_dotenv(properties_path)

if not properties_path.is_file():
    print(f"ERROR: The properties file was NOT found at {properties_path}")
else:
    load_success = load_dotenv(dotenv_path=properties_path, verbose=True)
    if load_success:
        print(f"Successfully loaded properties from {properties_path}")
    else:
        print(f"WARN: Failed to load properties.")

url = os.getenv("URL")
token = os.getenv("TOKEN")

# SCIM Standard for getting a single user: GET /Users/{id}
#scim_url = f"{url.rstrip('/')}/Users/{user_id}"

#get a user's groups
scim_url = f"{url.rstrip('/')}/Users/{user_id}?attributes=groups,emails,id,userName,active,name,displayName,externalId,roles,active"


headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/scim+json",
    "Accept": "application/scim+json"
}

try:
    # Use GET to retrieve the specific user resource
    response = requests.get(scim_url, headers=headers)

    if response.status_code == 200:
        print(f"\n--- User Found (ID: {user_id}) ---")
        # Pretty print the full SCIM user object
        print(json.dumps(response.json(), indent=4))
    elif response.status_code == 404:
        print(response.text)
        print(f"Error: User with ID {user_id} was not found (404).")
    else:
        print(f"Failed to retrieve user. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Network or API Error: {e}")