import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
from pandas import json_normalize
from datetime import datetime, timedelta

def request_ISO(application = 'genfuelmix/current'):
    '''
    :param application: the application as specified by ISO
    :return: a dicionary (usually) from that pull
    '''
    # Credentials
    username = 'sapozhnikov.i@northeastern.edu'
    password = 'Shark3Gum'

    # Make URL
    base_url = 'https://webservices.iso-ne.com/api/v1.1'
    endpoint = f'/{application}.json'
    # Full URL
    url = base_url + endpoint

    # Make the request
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        # Handle JSON response
        data = response.json()
        # Unncomment to dump json
        # print(json.dumps(data, indent=2))
        return data
    else:
        print('Failed to retrieve data:', response.status_code, f'from {url}')

def request_ISO_genfuelmix_day(date = datetime.now().strftime('%Y%m%d')):
    '''
    input a date in format YYYYMMDD
    return a dataframe of Genfuelmix data for that date
    '''
    # Use generic pull
    data = request_ISO(application=f'genfuelmix/day/{date}')
    # Return Dataframe instead of JSON
    df = json_normalize(data['GenFuelMixes']['GenFuelMix'])
    df['BeginDate'] = pd.to_datetime(df['BeginDate'])
    return df
def request_ISO_genfuelmix_daterange(beg_date = 20240101, end_date = datetime.now().strftime('%Y%m%d')):
    '''
    :param beg_date: in format YYYYMMDD
    :param end_date: in format YYYYMMDD
    :return: dataframe with Genfuelmix data for that date range
    '''
    data_frames= []

    # Convert the date strings to datetime objects
    start_date = datetime.strptime(str(beg_date), '%Y%m%d')
    end_date = datetime.strptime(str(end_date), '%Y%m%d')

    # Initialize the current date to start date
    current_date = start_date
    while current_date <= end_date:
        df = request_ISO_genfuelmix_day(current_date.strftime('%Y%m%d'))
        current_date += timedelta(days=1)  # Increment the day by one

        data_frames.append(df)

    final_df = pd.concat(data_frames, ignore_index=True)
    return final_df
