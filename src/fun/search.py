import requests


def search_anime(client_id, url, type, q, limit = 100, offset = 0, fields = ''):
    '''
    GET request to search in the MAL database
    :param client_id: Client ID of the MAL app
    :param url: MAL api link
    :param q: query of the search
    :param limit: limit of manga you want to get
    :param offset:
    :param fields: infos you want to get
    :return:
    '''
    url = url + type
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