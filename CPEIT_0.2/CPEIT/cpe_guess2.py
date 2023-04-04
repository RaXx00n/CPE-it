import json
import re

with open('Got-Combined.json', 'r') as f:
    data = json.load(f)

with open('PotentialCPE.txt', 'w') as f:
    for item in data:
        if 'Publisher' in item and item['Publisher']:
            vendor = item['Publisher'].lower().replace('the', '').split()[0]
        elif 'Vendor' in item and item['Vendor']:
            vendor = item['Vendor'].lower().replace('the', '').split()[0]
        else:
            continue  # Skip this item if neither Publisher nor Vendor is present or has no value
        if 'Name' in item and item['Name']:
            name = item['Name']
        elif 'DisplayName' in item and item['DisplayName']:
            name = item['DisplayName']
        else:
            continue  # Skip this item if neither Name nor DisplayName is present or has no value
        name_words = name.lower().replace('the', '').split()
        if vendor in name_words:
            name_words.remove(vendor)
        # Remove version numbers and vendor name from product name
        name_words = [word for word in name_words if not re.match(r'\d+(\.\d+)*', word) and word != vendor]
        product = name_words[0] if name_words and name_words[0] != '' else ''
        cpe_string = f'cpe:2.3:a:{vendor}:{product}:-:*:*:*:*:*:*:*'
        f.write(cpe_string + "\n")  # Write the CPE string to file
