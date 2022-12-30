import requests

def get_forum_board(client_id):
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }

    return requests.get('https://api.myanimelist.net/v2/forum/boards', headers=headers).json()


def get_topic_details(client_id, topic_id, limit, offset):
    url = f'https://api.myanimelist.net/v2/forum/topic/{topic_id}'
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }

    params = {
        'limit': limit,
        'offset': offset
    }

    return requests.get(url, headers=headers, params=params).json()


def get_forum_topics(client_id, kwargs):
    url = 'https://api.myanimelist.net/v2/forum/topics'
    headers = {
        'X-MAL-CLIENT-ID': client_id
    }
    params = {}
    for k, v in kwargs.items():
        params[k] = str(v)

    return requests.get(url, headers=headers, params=params).json()