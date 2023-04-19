import json

# Load the JSON file
with open('Got-Vulns.json', 'r') as file:
    data = json.load(file)

# Remove the specified keys from each dictionary in the list
for obj in data:
    del obj['Name']
    del obj['Version']
    del obj['ProviderName']
    del obj['Keyword']
    del obj['UninstallString']
    del obj['PotentialCPE']

    if obj.get('PRODUCTCPE'):
        obj['Approximate CPE'] = obj.pop('PRODUCTCPE')
    if obj.get('EXACTCPE'):
        obj['CPE'] = obj.pop('EXACTCPE')

    
# Save the modified JSON to a new file
with open('Cleaned.json', 'w') as file:
    json.dump(data, file, indent=2)
