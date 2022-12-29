import requests

def get_my_informations(TOKEN):
    headers = {
        'Authorization': 'Bearer ' + TOKEN
    }


    return requests.get('https://api.myanimelist.net/v2/users/@me', headers=headers).json()

