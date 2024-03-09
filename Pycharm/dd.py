import requests
import json
import datetime

# Define the API URL
api_url = "https://9rhjqf5ix7.execute-api.ap-south-1.amazonaws.com/dev/apicount?operation=add"

# Get the current datetime
current_datetime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

# Define the payload with the current datetime
payload = {
    "datetime": current_datetime,
    "api_name": "TaxCalculator_api",
    "customer_id": "20011069",
    "customer_name": "chinu41",
    "source": "TaxbaseLANPro",
    "ip": "192.168.0.156"
}

# Convert payload to JSON format
payload_json = json.dumps(payload)

# Send POST request to the API
response = requests.post(api_url, data=payload_json)

# Check if request was successful (status code 200)
if response.status_code == 200:
    print("API call successful.")
else:
    print(f"API call failed with status code: {response.status_code}")
