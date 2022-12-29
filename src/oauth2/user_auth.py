import requests


def get_token(client_id, code_challenge):
    parameters = {
        'response_type': 'code',
        'client_id': client_id,
        'code_challenge': code_challenge
    }

    response = requests.get('https://myanimelist.net/v1/oauth2/token', data = parameters)
    return (response.status_code, response.text)
