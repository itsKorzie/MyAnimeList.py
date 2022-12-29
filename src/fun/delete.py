import requests

def delete(access_token, type, id):
    url = 'https://api.myanimelist.net/v2/' + type + '/' + str(id) + '/my_list_status'
    headers = {
        'Authorization': 'Bearer ' + access_token,
    }

    return requests.delete(url, headers=headers).json()