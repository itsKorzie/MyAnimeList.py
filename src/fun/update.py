import requests

def update_list(access_token, type, id, kwargs):
    url = f'https://api.myanimelist.net/v2/{type}/{id}/my_list_status'
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    data = {}
    for k, v in kwargs.items():
        data[k] = str(v)

    return requests.put(url, headers=headers, data=data).json()