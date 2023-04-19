import requests

# You will need to change this address to your elk stack if you want to send data!
logstash_url = 'http://[ YOUR ELK ADDRESS HERE]:5000/'

# Define the path to the JSON file to send
json_file_path = 'Got-Combined.json'

# Read the JSON file data
with open(json_file_path, 'rb') as f:
    json_data = f.read()

# Send the JSON data to the Logstash listener
response = requests.post(logstash_url, data=json_data)

# Check the response status code
if response.status_code == 200:
    print('JSON data sent successfully.')
else:
    print('Failed to send JSON data.')
