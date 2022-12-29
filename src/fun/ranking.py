import requests

def get_ranking(url, client_id, type, ranking_type, limit=100, offset=0, fields=''):
    url = url + type + '/ranking'
    parameters = {
        'ranking_type': ranking_type,
        'limit': limit,
        'offset': offset,
        'fields': fields
    }
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }

    return requests.get('', params=parameters, headers=headers).json()