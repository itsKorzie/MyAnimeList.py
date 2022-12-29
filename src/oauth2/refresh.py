import requests

def refresh_keys(client_id, client_secret, refresh_token):
    parameters = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }

    res = requests.post('https://myanimelist.net/v1/oauth2/token', data=parameters).json()
    return (res['access_token'], res['refresh_token'])