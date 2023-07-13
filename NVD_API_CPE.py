import json
import nvdlib

# Load the contents of test3.json into a Python object
with open('Got-Keywords.json', 'r') as f:
    data = json.load(f)

# Loop through each object in the data
for obj in data:
    # Get the DisplayName from the current object
    keyword = obj['Keyword']

    # Use the nvdlib to search for CPEs matching the DisplayName
    results = nvdlib.searchCPE(keywordSearch=keyword, key='63b875a4-a426-40ea-b97d-add230444390', delay=0.6)

    # Create a list of potential CPEs from the search results
    potential_cpes = [cpe.cpeName for cpe in results]

    # Add the potential CPEs list to the current object as a new key/value pair
    obj['PotentialCPE'] = potential_cpes

# Save the updated data to Got-CPE.json
with open('Got-CPE.json', 'w') as f:
    json.dump(data, f, indent=2)
