from flask import Flask, redirect, request, render_template
import requests

app2 = Flask(__name__)

# Configuration for LINE Login
CLIENT_ID = '2004694759'
CLIENT_SECRET = '0bdd583ebad18cad9643adddcd39f732'
REDIRECT_URI = 'http://127.0.0.1:5000/login2' #'http://localhost:5000/callback'
AUTH_URL = 'https://access.line.me/oauth2/v2.1/authorize'

@app2.route('/')
def index():
    return render_template('index.html')

@app2.route('/login2')
def login2():
    # Redirect the user to the LINE Login page
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': 'some_random_state',
        'scope': 'openid profile',
    }
    auth_url = f"{AUTH_URL}?{'&'.join([f'{key}={value}' for key, value in params.items()])}"
    return render_template('login2.html', auth_url=auth_url)

@app2.route('/callback')
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
            return "Login successful! Access token: " + access_token
    return "Failed to login"

if __name__ == '__main__':
    app2.run(debug=True)
