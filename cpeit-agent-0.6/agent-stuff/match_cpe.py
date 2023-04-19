import json
import re
from collections import Counter

# Read in the data from test4.json
with open('Got-CPE.json', 'r') as f:
    data = json.load(f)

# Loop through each object in the data
for obj in data:
    # Get the DisplayVersion field, removing non-number characters
    display_version = re.sub(r'[^\d]', '', obj['DisplayVersion'])

    # If there are no PotentialCPE values, skip to the next object
    if not obj.get('PotentialCPE'):
        continue

    # Find the PotentialCPE that matches the DisplayVersion exactly
    exact_match = None
    product_cpe = None
    vendor_counts = Counter()
    for cpe in obj['PotentialCPE']:
        # Extract the vendor and product names from the CPE
        match = re.match(r'^cpe:2\.3:a:([^:]+):([^:]+):([^:]+):', cpe)
        if not match:
            continue
        vendor = match.group(1)
        product = match.group(2)
        cpe_version = re.sub(r'[^\d]', '', match.group(3))

        if cpe_version == display_version:
            exact_match = cpe
        elif not cpe_version:
            vendor_counts[f"cpe:2.3:a:{vendor}:{product}"] += 1

    # Save the closest PotentialCPE as a new field called EXACTCPE or PRODUCTCPE
    if exact_match:
        obj['EXACTCPE'] = exact_match
    elif vendor_counts:
        product_vendor = vendor_counts.most_common(1)[0][0]
        obj['PRODUCTCPE'] = f"{product_vendor}:*:*:*:*:*:*:*:*"

# Save the updated data as test4_updated.json
with open('Matched-CPE.json', 'w') as f:
    json.dump(data, f, indent=4)
