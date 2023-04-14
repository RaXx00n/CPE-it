import requests
import json
import time

# Define the base URL for the NVD NIST API
base_url = 'https://services.nvd.nist.gov/rest/json/cpes/1.0'

# Define your API key
api_key = 'a388573e-694d-4368-98d0-7118366fc7ba'

# Open the input file
with open('PotentialCPE.txt', 'r') as input_file:
    # Loop over each line in the input file
    for line in input_file:
        # Remove any leading or trailing whitespace from the line
        line = line.strip()
        # Build the API request URL for this line, including your API key
        url = f'{base_url}?cpeMatchString={line}&apiKey={api_key}'
        # Send the API request and get the response
        response = requests.get(url)
        # Parse the JSON response into a Python dictionary
        response_dict = json.loads(response.content)
        # Print the response dictionary to the console
        print(response_dict)
        # Sleep for 3 seconds before making the next request
        time.sleep(6)
