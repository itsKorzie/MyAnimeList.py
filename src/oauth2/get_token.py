import requests


def get_token(client_id, code, code_verifier,client_secret=''):
    parameters = {
        'client_id': client_id,
        'code': code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    if client_secret != '':
        parameters['client_secret'] = client_secret

    response = requests.post('https://myanimelist.net/v1/oauth2/token', data = parameters).json()

    try:
        return (response['access_token'], response['refresh_token'])
    except:
        print('Error, you may enter the client_secret')
        raise