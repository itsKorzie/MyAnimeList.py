import requests


def get_token(client_id, client_secret, code, code_verifier):
    parameters = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post('https://myanimelist.net/v1/oauth2/token', data = parameters).json()

    return (response['access_token'], response['refresh_token'])