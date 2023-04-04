import json

# Open the files
with open("Got-Item.json", "r", encoding="utf-8-sig") as item_file:
    item_data = json.load(item_file)

with open("Got-Package.json", "r", encoding="utf-8-sig") as package_file:
    package_data = json.load(package_file)
    
with open("Got-WmiObject.json", "r", encoding="utf-8-sig") as wmi_file:
    wmi_data = json.load(wmi_file)

# Create a new list to store the combined data
combined_data = []

# Loop over the item data
for item in item_data:
    # Get the name or display name
    name = item.get("DisplayName", item.get("Name"))
    
    # Search for the name in the package data
    for package in package_data:
        if package.get("Name") == name:
            # Combine the data
            combined_item = {**item, **package}
            combined_data.append(combined_item)
            break

# Write the combined data to a file
with open("Got-Combined.json", "w", encoding="utf-8") as combined_file:
    json.dump(combined_data, combined_file, indent=4)
