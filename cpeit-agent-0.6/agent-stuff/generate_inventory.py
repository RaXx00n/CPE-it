import json
import pandas as pd
import urllib.parse

# Load data from Cleaned.json file
with open('Got-Combined.json') as f:
    data = json.load(f)

# Extract required fields from data
rows = []
for item in data:
    row = {
        'Name': item.get('DisplayName', ''),
        'Version': item.get('DisplayVersion', ''),
        'Publisher': item.get('Publisher', ''),
        'Install Date': item.get('InstallDate', ''),
        'Location': item.get('InstallLocation', ''),
        'Uninstall String': item.get('UninstallString', ''),
    }
    rows.append(row)

# Create table using pandas
df = pd.DataFrame(rows, columns=['Name', 'Version', 'Publisher', 'Install Date', 'Location', 'Uninstall String'])
table_html = df.to_html(index=False, escape=False)

# Add CSS styling to table
table_style = '''
<style>
    table {
        border-collapse: collapse;
        width: 100%;
        color: #fff;
        background-color: #202020;
    }
    th, td {
        text-align: left;
        padding: 8px;
        border: 1px solid #ddd;
    }
    tr:nth-child(even) {
        background-color: #2d2d2d;
    }
    th {
        background-color: #292929;
    }
    a {
    color: cyan;
    }
    a:visited {
    color: cyan;
    }
</style>
'''

table_html = table_style + table_html

# Save table to Report.html file
with open('Software-Inventory.html', 'w') as f:
    f.write(table_html)
