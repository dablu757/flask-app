from flask import Flask, redirect, url_for, render_template, request, session, flash
from common import success_responce, error_responce
from logger import LOGGER
from dotenv import load_dotenv
import os
from datetime import timedelta
import sqlalchemy

load_dotenv()
_secreate_key = os.getenv('SECRET_KEY')
_debug_mode = os.getenv('DEBUG', 'False')

app = Flask(__name__)
app.secret_key = _secreate_key
app.permanent_session_lifetime = timedelta(seconds=10)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        _user = request.form['nm']
        session['user'] = _user
        flash(f'Welcome, {_user}!', 'success') 
        return redirect(url_for('user'))
    else:
        return render_template('login.html')
    
@app.route("/logout")
def logout():
    if "user" in session:
        flash('You have been logged out!', 'info')
        session.pop('user', None)
    return redirect(url_for('login'))

@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=_debug_mode
    )
