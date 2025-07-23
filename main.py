from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_strong_random_secret_key_here_CHANGE_THIS!'

DB_CONFIG = {
    "host": "localhost",
    "port": 3307,
    "user": "root",
    "password": "",
    "database": "edugradedb"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    return render_template('login.html')


@app.route('/users_signup')
def user_signup():
    return render_template('sign_up.html')  # Renders the signup form



if __name__ == '__main__':
    app.run(debug=True)
