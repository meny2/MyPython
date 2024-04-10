from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to the SQLite database
conn = sqlite3.connect('inventory.db', check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')

# Function to check if user is logged in
def is_logged_in():
    return 'username' in session

# Route for the login page
@app.route('/')
def login():
    if is_logged_in():
        return redirect('/dashboard')
    return render_template('login.html')

# Route for handling login
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    if user:
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('login.html', error='Invalid username or password')

# Route for the dashboard
@app.route('/dashboard')
def dashboard():
    if is_logged_in():
        cursor.execute("SELECT * FROM inventory")
        inventory = cursor.fetchall()
        return render_template('dashboard.html', inventory=inventory)
    else:
        return redirect('/')

# Route for logging out
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
