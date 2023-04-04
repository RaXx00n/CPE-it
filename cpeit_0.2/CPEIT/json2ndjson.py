import json

# Set up file paths
input_path = 'Got-Combined.json'
output_path = 'Got-Delimited.ndjson'

# Read in JSON data
with open(input_path, 'r') as f:
    data = json.load(f)

# Write out NDJSON data
with open(output_path, 'w') as f:
    for record in data:
        f.write(json.dumps(record) + '\n')
