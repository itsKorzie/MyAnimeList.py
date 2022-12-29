import requests

def get_user_list(access_token, type, user_name, kwargs):
    url = f'https://api.myanimelist.net/v2/users/{user_name}/{type}list'
    print(url)
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    params = {}
    for k, v in kwargs.items():
        params[k] = str(v)

    return requests.get(url, headers=headers, params=params).json()

