#pip install requests
#https://notify-bot.line.me/en/

import requests

def send_line_notify(message, token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    data = {'message': message}
    r = requests.post(url, headers=headers, data=data)
    return r.status_code


