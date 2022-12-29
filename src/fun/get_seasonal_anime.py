import requests

def get_seasonal_anime(url,client_id, year, season, sort, limit, offset, fields):
    url = f'{url}fun/season/{str(year)}/{season}'

    parameters = {
        'sort': sort,
        'limit': limit,
        'offset': offset,
        'fields': fields
    }
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }

    return requests.get(url, params=parameters, headers=headers).json()