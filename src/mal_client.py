from search import *
from get_anime_details import *


class Client():
    def __init__(self, client_id):
        self.client_id = client_id

    def search(self, q, limit=100, offset=0, fields=''):
        url = 'https://api.myanimelist.net/v2/anime'
        response = search.search(self.client_id, url, q, limit, offset, fields)
        return response

    def get_anime_details(self, anime_id, fields=''):
        url = 'https://api.myanimelist.net/v2/anime/'
        response = get_anime_details(url, self.client_id, anime_id, fields)
        return response


