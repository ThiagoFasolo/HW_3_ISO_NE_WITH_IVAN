import requests
from requests.auth import HTTPBasicAuth
import json
import xml.etree.ElementTree as ET
from pandas import json_normalize
import sandkey
import Basic_Table
from Basic_Table import create_table

username = 'sapozhnikov.i@northeastern.edu'
password = 'Shark3Gum'
base_url = 'https://webservices.iso-ne.com/api/v1.1'

# edit this
date = '20241012'
application = f'genfuelmix/day/{date}'
endpoint = f'/{application}.json'

url = base_url + endpoint

# Make the request
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if the request was successful
if response.status_code == 200:
    if endpoint.endswith('.json'):
        # Handle JSON response
        data = response.json()
        print(json.dumps(data, indent=2))
    elif endpoint.endswith('.xml'):
        # Handle XML response
        root = ET.fromstring(response.content)
        print(ET.tostring(root, encoding='utf8').decode('utf8'))
else:
    print('Failed to retrieve data:', response.status_code)

df = json_normalize(data['GenFuelMixes']['GenFuelMix'])

col2 = 'FuelCategoryRollup'
col1 = 'FuelCategory'
word = 'NonRenewable'

df[col2] = df.apply(lambda row: word if row[col1] == row[col2] else row[col2], axis=1)
create_table(df)

sandkey.make_sankey(df, columns=['FuelCategoryRollup', 'FuelCategory'], vals_col='GenMw')