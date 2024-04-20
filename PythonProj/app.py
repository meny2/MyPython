from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta
import random
import string
import smtplib, ssl
import os
from email.message import EmailMessage
from connect_db import connect_to_database, verify_user_login, verify_email, update_password, insert_user
from valid_email import is_valid_email
from line_messaging_api import send_line_message
from line_notify import send_line_notify
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route สำหรับหน้า home
@app.route('/')
def home():
    return render_template('home.html')

# Route สำหรับการ login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        connection = connect_to_database()

        # Verify user login
        if connection:            
            if verify_user_login(connection, username, password):
                return redirect(url_for('main_menu',username=username))
            else:
                return render_template('home.html', error='Invalid username or password')            
        # Close the database connection
        if connection:
            connection.close()
            
    return redirect(url_for('home'))
    

# Route สำหรับหน้า main menu
@app.route('/main_menu')
def main_menu():
    username = request.args.get('username')
    return render_template('main_menu.html',username=username)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


def generate_random_password():
    # สร้างรหัสผ่านสุ่ม
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))

def send_password_reset_email(email, new_password):
    # กำหนดข้อมูลเกี่ยวกับอีเมลผู้ส่งและผู้รับ
    sender_email = "adisornsophon.n@gmail.com"    #sgnglobal02@gmail.com Synergy@02
    password = "men_127018"
    receiver_email = email

    subject = "Your New Password"
    # เนื้อหาของอีเมล
    body = f"Your new password is: {new_password}"

    # สร้างอีเมล
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    context = ssl.create_default_context()

    # เชื่อมต่อกับเซิร์ฟเวอร์ SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as server:        
        server.login(sender_email, "qxqybmslilaliwzf") # ส่งอีเมล google app (รหัสผ่านสำหรับแอป)        
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.form.get('email')
    if is_valid_email(email):       
         # Connect to the database
        connection = connect_to_database()

        # Verify email
        if connection:
            if verify_email(connection, email) == email:
                new_password = generate_random_password() # สร้างรหัสผ่านใหม่สำหรับผู้ใช้งาน 
                update_password(connection, email, new_password)  # บันทึกรหัสผ่านใหม่ลงในฐานข้อมูลหรือรายการลืมรหัสผ่าน              
                send_password_reset_email(email, new_password) # ส่งอีเมลหรือข้อความรหัสผ่านใหม่ไปยังผู้ใช้งาน                
                return redirect(url_for('home')) # นำผู้ใช้งานไปยังหน้าตั้งค่าบัญชีหรือหน้าที่สะดวก
            else:
                error = 'Email not found'
                return render_template('forgot_password.html', error=error)          
        # Close the database connection
        if connection:
            connection.close()  
    else:
        print(f"The email '{email}' does not have a valid format.")
        return render_template('forgot_password.html')

@app.route('/registration_user')
def registration_user():
    return render_template('registration_user.html')

@app.route('/registration_add', methods=['POST'])
def registration_add():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if is_valid_email(email):       
         # Connect to the database
        connection = connect_to_database()

        # Verify email
        if connection:
            if verify_email(connection, email) != email:                
                insert_user(connection, username, email, password)  # บันทึกรหัสผ่านใหม่ลงในฐานข้อมูลหรือรายการลืมรหัสผ่าน              
                return redirect(url_for('home')) # นำผู้ใช้งานไปยังหน้าตั้งค่าบัญชีหรือหน้าที่สะดวก
            else:
                error = 'There is an email in the system. Please enter new email again.'
                return render_template('registration_user.html', error=error)          
        # Close the database connection
        if connection:
            connection.close()  
    else:
        print(f"The email '{email}' does not have a valid format.")
        return render_template('registration_user.html')

@app.route('/line_notify')
def line_notify():
    # เรียกใช้งานฟังก์ชันเพื่อส่งข้อความ https://notify-bot.line.me/th/  (Menu > Mypage)
    token = '6jx70dXAMNtE79HzanZec4JynVLfEC5B5JLXic0mwxp'  
    message = 'Hello, ส่งข้อความผ่าน Python มาแล้ว!'
    send_line_notify(message, token)    
    return redirect(url_for('home'))

@app.route('/line_messaging_api')
def line_messaging_api():
    # เรียกใช้งานฟังก์ชัน send_line_message โดยกำหนด access token และข้อความที่ต้องการส่ง
    #access_token = 'WG8k57uXmx5Zh8alAdgV5WMVDdaTEANoWNS1JE2EyN2i1AMSfVa+++HQ2ngtxq87V9AzF0TmtUNhbO7X/SXGVVgGTvh7Xh5ydXDVY+yssUrmveA6VIFJwNBWL+m8tO4c8YmhAZOUKkqDxgoWoTh1QgdB04t89/1O/w1cDnyilFU='
    access_token = 'TyehqT2uC7wyXBslk5T1f9khtLpGXId5+az9vLX7wQnK6Bs5NQsfbA5rcYzNaV6SkC5CwKJRMHf0yPQ0X2/YAtyb2v776gy3GnShZK18aDh4Jw7JN6ONkvwTYDvIl0d9RUtT+CK30ghg03ZPVeNBegdB04t89/1O/w1cDnyilFU='
    user_id = 'U95823232d2a38ada5a3cc379cbd47710'
    message = 'Hello, World!'
    send_line_message(access_token, user_id, message)    
    return redirect(url_for('home'))

# Configuration for LINE Login
CLIENT_ID = '2004694759'
CLIENT_SECRET = '0bdd583ebad18cad9643adddcd39f732'
REDIRECT_URI = 'http://127.0.0.1:5000/callback'
AUTH_URL = 'https://access.line.me/oauth2/v2.1/authorize'
PROFILE_URL = 'https://api.line.me/v2/profile'

@app.route('/line_login')
def line_login():  
    # Redirect the user to the LINE Login page
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': 'some_random_state',
        'scope': 'openid profile',
    }
    auth_url = f"{AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return redirect(auth_url)
    #return render_template('line_login.html', auth_url=auth_url)    

@app.route('/callback')
def callback():
    # Handle the callback from LINE Login
    code = request.args.get('code')    
    if code:
        # Exchange the code for an access token
        token_url = 'https://api.line.me/oauth2/v2.1/token'
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
        response = requests.post(token_url, data=data)
        if response.ok:
            access_token = response.json()['access_token']            
            # Now you have the access token, you can use it to make requests to the LINE API
            #return "Login successful! Access token: " + access_token
        
            # Use the access token to get the user's profile
            headers = {'Authorization': f'Bearer {access_token}'}
            profile_response = requests.get(PROFILE_URL, headers=headers)
            if profile_response.ok:
                user_id = profile_response.json()['userId']
                # Now you have the LINE user ID
                return f"LINE user ID: {user_id}"
            
    return "Failed to login"

if __name__ == '__main__':
    app.run(debug=True)

# app.permanent_session_lifetime = timedelta(minutes=30)  # Session timeout set to 30 minutes