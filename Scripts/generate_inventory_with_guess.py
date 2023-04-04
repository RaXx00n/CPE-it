import json
import datetime
from json2html import json2html
from json2html import *

# Validate the JSON file
with open('Got-Combined-with-Guess.json') as f:
    try:
        data = json.load(f)
        print("JSON is valid")
    except json.decoder.JSONDecodeError as e:
        print("JSON is invalid")
        print(str(e))

# Define a custom transformation to remove the Name and Version fields
def remove_fields(data):
    if isinstance(data, list):
        for item in data:
            remove_fields(item)
    elif isinstance(data, dict):
        if 'Name' in data:
            del data['Name']
        if 'Version' in data:
            del data['Version']
        for key, value in data.items():
            remove_fields(value)

# Convert the JSON to HTML
with open('Got-Combined-with-Guess.json', encoding='utf-8-sig') as f:
    data = json.load(f)
    remove_fields(data)
    table = json2html.convert(json = data)

# Save the HTML output to a file
output_filename = f"Software-Inventory-CPE.html"
with open(output_filename, 'w') as f:
    f.write(table)
