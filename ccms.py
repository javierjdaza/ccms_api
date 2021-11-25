# Importing Libraries
import requests
import json
import base64
from getpass import getpass



def ccms_auth(user_id:str,password:str):
    url = 'https://oauth.teleperformance.co/api/oauthlogin'

    # contraseña = 'Diciembre2020*'
    cadena = '{"user":' + '"' + user_id+ '"' + ',"pass":' + '"' + password + '"}'

    enc = cadena.encode()
    x = base64.b64encode(enc).decode('utf-8')
    cadena_codificada = 't' + x

    data = {
        "body": cadena_codificada,
        "project": "Test",
        "ip": "123d4",
        "uri": "aptp",
        "size": 0
    }

    try:
        r = requests.post(url, data=data)
        json_gen = json.loads(r.text)
        
    except Exception as e:
        print(e)

    print(json_gen)
    return json_gen


def main():
    user_id = getpass('CCMS ID:\n')
    password = getpass('PASSWORD: \n')
    ccms_auth(user_id,password)


if __name__ == '__main__':
    main()