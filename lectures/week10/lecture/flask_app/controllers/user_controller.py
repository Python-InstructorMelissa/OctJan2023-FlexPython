from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User
from flask_app.models.image_model import Image



@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('logReg.html')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theUsers = User.getAll()
        theImages = Image.getAll()
        return render_template('index.html', user=theUser, users=theUsers, images=theImages)
    
@app.route('/user/create/', methods=['post'])
def createUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'username': request.form['username'],
        'email': request.form['email']
    }
    id = User.save(data)
    if not id:
        return redirect('/')
    else:
        session['user_id'] = id
        return redirect('/')

@app.route('/user/login/', methods=['post'])
def login():
    data = {
        'username': request.form['username']
    }
    user = User.getUsername(data)
    if not user:
        return redirect('/')
    else:
        session['user_id'] = user.id
        return redirect('/')
    
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')