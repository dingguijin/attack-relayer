import requests
import json

# Define the URL where you want to send the JSON data
url = "https://tornado.vin/d692ae63-0a7e-43e0-9da9-fe4f4cc6c607"

# Create a dictionary with your JSON data
data = {
    "key1": "value1",
    "key2": "value2"
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Set the headers to indicate that you're sending JSON data
headers = {"Content-Type": "application/json"}

# Send a POST request with the JSON data
response = requests.post(url, data=json_data, headers=headers)

# Check the response
if response.status_code == 200:
    print("Request was successful")
    print("Response:", response.text)
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)

