import json
import pandas as pd
import urllib.parse

# Load data from Cleaned.json file
with open('Cleaned.json') as f:
    data = json.load(f)

# Extract required fields from data
rows = []
for item in data:
   
    cpe_list = [item.get('CPE', '') + item.get('Approximate CPE', '')]
    cpe_link_list = ['<a href="https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=' + urllib.parse.quote(cpe, safe='') + '">' + cpe + '</a>' for cpe in cpe_list]
    cpe_links = '<br>'.join(cpe_link_list)
    cve_list = item.get('NVD_RESULTS', {})
    cve_link_list = ['<a href="https://nvd.nist.gov/vuln/detail/' + cve + '">' + cve + '</a>' for cve in cve_list if cve]
    cve_links = '<br>'.join(cve_link_list)
    row = {
        'DisplayName': item.get('DisplayName', ''),
        'DisplayVersion': item.get('DisplayVersion', ''),
        'Publisher': item.get('Publisher', ''),
        'InstallDate': item.get('InstallDate', ''),
        'InstallLocation': item.get('InstallLocation', ''),
        'CPE': cpe_links,
        'CVE': cve_links
    }
    rows.append(row)

# Create table using pandas
df = pd.DataFrame(rows, columns=['DisplayName', 'DisplayVersion', 'Publisher', 'InstallDate', 'InstallLocation', 'CPE', 'CVE'])
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
with open('NVD-Inventory.html', 'w') as f:
    f.write(table_html)
