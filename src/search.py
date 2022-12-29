import requests


def search(client_id, url, q, limit = 100, offset = 0, fields = ''):
    parameters = {
        'q': q,
        'limit': limit,
        'offset': offset,
        'fields': fields
    }
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }

    res = requests.get(url, params=parameters, headers=headers)
    res = res.json()
    return res