from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LogInForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User Jason'}
    return render_template('index.html', title = 'Home', user = user)

@app.route('/test')
def test():
    return 'This is a test'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LogInForm()
    return render_template('login.html', title='Sign In', form=form)