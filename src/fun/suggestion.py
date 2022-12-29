import requests

def get_suggested(access_token, type, limit, offset, fields):
    url = f'https://api.myanimelist.net/v2/{type}/suggestions'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    params = {
        'limit': limit,
        'offset': offset,
        'fields': fields
    }

    return requests.get(url, headers=headers, params=params).json()