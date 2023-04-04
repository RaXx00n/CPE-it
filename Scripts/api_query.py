import requests

with open('formatted_cpes.txt', 'r') as f:
    for line in f:
        url = f'https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword={line.strip()}'
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f'Error: {response.status_code} - {response.reason}')
