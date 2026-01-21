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
    # Use verbose=True to get feedback on the loading process
    load_success = load_dotenv(dotenv_path=properties_path, verbose=True)
    if load_success:
        print(f"Successfully loaded properties from {properties_path}")
    else:
        print(f"WARN: Failed to load properties, but file exists. Check file format.")

url = os.getenv("URL")
token = os.getenv("TOKEN")


scim_url = f"{url.rstrip('/')}/Users/{user_id}"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/scim+json"
}

try:
    # Use DELETE to remove the resource
    response = requests.delete(scim_url, headers=headers)

    # 204 No Content is the standard success for DELETE in SCIM
    if response.status_code == 204:
        print(f"Status code returned: {response.status_code}")
        print("Successfully deleted user. (No response body returned for 204)")

    # Handle other success codes like 200 OK that might include a body
    elif response.status_code == 200:
        print(f"Status code returned: {response.status_code}")
        print("Successfully deleted user:")
        # Check if there is actual text before parsing JSON
        if response.text:
            print(json.dumps(response.json(), indent=4))

    else:
        print(f"Failed to delete user. Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Network or API Error: {e}")
