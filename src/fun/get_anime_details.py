import requests


def get_anime_details(url,client_id, type, id, fields=''):
    url = url + type + '/' + str(id)
    parameters = {
        'fields': fields
    }
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }
    res = requests.get(url, params=parameters, headers=headers)
    res = res.json()
    return res

