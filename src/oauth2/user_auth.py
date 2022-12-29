import requests
import webbrowser


def open_web(client_id, code_challenge):
    url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={client_id}&code_challenge={code_challenge}&state=RequestID42'
    webbrowser.open(url, new=1)

