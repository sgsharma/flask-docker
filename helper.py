import json

import requests


def get_activity(**kwargs):
    BASE_URL = 'https://www.boredapi.com/api/activity/'
    if kwargs.get('activity_type') is not None:
        params = {'type': kwargs.get('activity_type')}
    else:
        params = None
    try:
        response = requests.request("GET", 
                                    BASE_URL, 
                                    params=params
                                    )
    except requests.exceptions.RequestException as e:
        print(e)
    return response