import json
import re

with open('Got-Combined.json', 'r') as f:
    data = json.load(f)

for item in data:
    if 'Publisher' in item:
        vendor = item['Publisher'].split()[0].lower()
    elif 'Vendor' in item:
        vendor = item['Vendor'].split()[0].lower()
    else:
        continue  # Skip this item if neither Publisher nor Vendor is present
    if 'Name' in item:
        name = item['Name']
    elif 'DisplayName' in item:
        name = item['DisplayName']
    else:
        continue  # Skip this item if neither Name nor DisplayName is present
    name_words = name.split()
    if vendor in name_words:
        name_words.remove(vendor)
    # Remove version numbers and vendor name from product name
    name_words = [word for word in name_words if not re.match(r'\d+(\.\d+)*', word) and word.lower() != vendor]
    product = ' '.join(name_words[:2]).lower()
    cpe_string = f'cpe:2.3:a:{vendor}:{product}:-:*:*:*:*:*:*:*'
    print(cpe_string)
