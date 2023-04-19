import json
import nvdlib

# Load the contents of test3.json into a Python object
with open('Matched-CPE.json', 'r') as f:
    data = json.load(f)

# Loop through each object in the data
for obj in data:
    # Check if the current object has an EXACTCPE key
    if 'EXACTCPE' not in obj:
        # If it doesn't, skip to the next object
        continue

    # Get the CPEe from the current object
    cpeID = obj['EXACTCPE']

    # Use the nvdlib to search for CPEs matching the DisplayName
    results = nvdlib.searchCVE(cpeName=cpeID, key='3bbbf3ec-80a1-42ff-bbd7-6ef739f7c059 ', delay=0.6)

    # Create a list of potential CVEs from the search results
    CVEs = [cve.id for cve in results]

    # Add the associated CVEs list to the current object as a new key/value pair
    obj['NVD_RESULTS'] = CVEs


# Save the updated data to test4.json
with open('Got-Vulns.json', 'w') as f:
    json.dump(data, f, indent=2)
