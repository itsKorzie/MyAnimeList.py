import requests


def get_token(client_id, client_secret, code, code_verifier):
    parameters = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'code_verifier': code_verifier,
        'grant_type': 'authorization_code'
    }

    response = requests.post('https://myanimelist.net/v1/oauth2/token', data = parameters)

    print(response.status_code)  # 200
    print(response.text)  # { ...Access Token... }