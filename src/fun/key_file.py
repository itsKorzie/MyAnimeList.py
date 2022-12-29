def make_key_file(client_id, pcke, code, access, refresh_token):
    file = open('keys.py', 'w')
    file.write('CLIENT_ID = \'' + client_id + '\'\nPCKE_CODE = \'' + pcke + '\'\nAUTH_CODE = \'' + code + '\'\nACCESS_TOKEN = \'' + access + '\'\nREFRESH_TOKEN = \'' + refresh_token + '\'')
    file.close()