from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User


@app.route('/dashboard/')
def index():
    data = {
        'id': session['user_id']
    }
    theUser = User.get_one(data)
    return render_template('index.html', user=theUser)

@app.route('/')
def logReg():
    return render_template('logReg.html')

@app.route('/registration/', methods=['post'])
def registration():
    newUser = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'username': request.form['username'],
        'email': request.form['email']
    }
    id = User.save(newUser)
    session['user_id'] = id
    return redirect('/dashboard/')

@app.route('/login/', methods=['post'])
def login():
    pass