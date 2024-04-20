#pip install line-bot-sdk
#ngrok ใช้เป็น Web Hook ในการส่งข้อมูล หรือ ให้คนอื่น เข้าใช้งานเครื่องเราได้

import requests

def send_line_message(access_token, user_id, message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    data = {
        'to': user_id,
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message. Status code:", response.status_code)

