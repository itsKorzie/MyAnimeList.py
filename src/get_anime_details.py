import requests


def get_anime_details(url,client_id, anime_id, fields=''):
    parameters = {
        'fields': fields
    }
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }
    url = url + anime_id
    res = requests.get(url, params=parameters, headers=headers)
    res = res.json()
    return res

