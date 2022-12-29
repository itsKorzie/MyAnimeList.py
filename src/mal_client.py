from fun import get_anime_details, get_seasonal_anime, ranking, search, key_file, informations
from oauth2 import pcke, user_auth, server, get_token, refresh
import os.path

class Client():
    def __init__(self, client_id, client_secret='', oauth=False, refresh_key=False):
        self.client_id = client_id
        self.url = 'https://api.myanimelist.net/v2/'
        if oauth:
            file_exist = os.path.exists('keys.py')
            if file_exist:
                import keys
                self.pcke_token = keys.PCKE_CODE
                self.code = keys.AUTH_CODE
                self.ACCESS_TOKEN = keys.ACCESS_TOKEN
                self.REFRESH_TOKEN = keys.REFRESH_TOKEN
                if refresh_key:
                    self.ACCESS_TOKEN, self.REFRESH_TOKEN = refresh.refresh_keys(self.client_id,client_secret, self.REFRESH_TOKEN)
            else:
                print('‼️No keys file found, new connection...')
                self.pcke_token = pcke.get_new_code_verifier()
                print('Opening your browser... please connect')
                user_auth.open_web(self.client_id, self.pcke_token)
                server.run_server()
                file = open('keys.py', 'r')
                self.code = file.read()
                file.close()
                self.ACCESS_TOKEN, self.REFRESH_TOKEN = get_token.get_token(self.client_id, client_secret, self.code, self.pcke_token)
                key_file.make_key_file(self.client_id, self.pcke_token, self.code, self.ACCESS_TOKEN, self.REFRESH_TOKEN)
                print('✔️Keys.py created')

    def search(self, type, q, limit=100, offset=0, fields=''):
        return search.search_anime(self.client_id, self.url,type, q, limit, offset, fields)

    def get_details(self, type, id, fields=''):
        return get_anime_details.get_anime_details(self.url, self.client_id, type, id, fields)

    def ranking(self, type, ranking_type, limit=100, offset=0, fields=''):
        return ranking.get_ranking(self.url, self.client_id, type, ranking_type, limit, offset, fields)

    def seasonal_anime(self, year, season, sort='anime_score', limit=100, offset=0, fields=''):
        return get_seasonal_anime.get_seasonal_anime(self.url, self.client_id, year, season, sort, limit, offset, fields)

    def my_informations(self):
        return informations.get_my_informations(self.ACCESS_TOKEN)


