import requests

def update_list(access_token, type, id, kwargs):
    url = f'https://api.myanimelist.net/v2/{type}/{str(id)}/my_list_status'
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    data = {}
    for k, v in kwargs.items():
        data[k] = str(v)

    return requests.put('https://api.myanimelist.net/v2/anime/17074/my_list_status', headers=headers, data=data).json()