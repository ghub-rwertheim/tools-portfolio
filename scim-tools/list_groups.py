import os
import requests
from pathlib import Path
from dotenv import load_dotenv

props = "test.props"

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

scim_url = f"{url.rstrip('/')}/Groups"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/scim+json"
}

# Pagination configuration
start_index = 1
items_per_page = 100
all_groups = []

print("Starting paginated user search...")

try:
    while True:
        params = {
            #"attributes": "id,userName,displayName",
            "startIndex": start_index,
            "count": items_per_page
        }

        response = requests.get(scim_url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        resources = data.get("Resources", [])
        total_results = data.get("totalResults", 0)

        if not resources:
            break

        all_groups.extend(resources)
        print(f"Retrieved {len(all_groups)} of {total_results} groups...")

        # Stop if we've collected all available users
        if len(all_groups) >= total_results:
            break

        # Increment start_index for the next page
        start_index += len(resources)

    # Process final list
    if all_groups:
        for group in all_groups:
            print(group)
            #print(f"User: {user.get('userName')} (ID: {user.get('id')})")
    else:
        print("No groups found.")

except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")