import requests

# Replace with your credentials
username = 'sapozhnikov.i@northeastern.edu'
password = 'Shark3Gum'

# Example API endpoint (use .json for JSON response)
url = 'https://webservices.iso-ne.com/api/v1.1/hourlysysload/current'

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    try:
        data = response.json()
    except ValueError:
        print("Error decoding JSON response.")
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # To see the raw response