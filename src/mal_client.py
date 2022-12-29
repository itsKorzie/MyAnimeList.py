from fun import get_anime_details, get_seasonal_anime, ranking, search


class Client():
    def __init__(self, client_id):
        self.client_id = client_id
        self.url = 'https://api.myanimelist.net/v2/'

    def search(self, type, q, limit=100, offset=0, fields=''):
        return search.search_anime(self.client_id, self.url,type, q, limit, offset, fields)

    def get_details(self, type, id, fields=''):
        return get_anime_details.get_anime_details(self.url, self.client_id, type, id, fields)

    def ranking(self, type, ranking_type, limit=100, offset=0, fields=''):
        return ranking.get_ranking(self.url, self.client_id, type, ranking_type, limit, offset, fields)

    def seasonal_anime(self, year, season, sort='anime_score', limit=100, offset=0, fields=''):
        return get_seasonal_anime.get_seasonal_anime(self.url, self.client_id, year, season, sort, limit, offset, fields)

