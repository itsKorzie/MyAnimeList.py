import requests

parameters = {
    'client_id': 'xxx',
    'client_secret': 'xxx',
    'grant_type': 'authorization_code',
    'refresh_token': 'xxx'
    }

response = requests.post('https://myanimelist.net/v1/oauth2/token', data = parameters)

print(response.text)