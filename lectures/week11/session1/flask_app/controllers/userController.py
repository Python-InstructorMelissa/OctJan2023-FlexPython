from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models.userModel import User
from flask_app.models.animalModel import Animal




@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('logReg.html')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theAnimals = Animal.getAll()
        return render_template('index.html', user=theUser, animals=theAnimals)

@app.route('/user/create/', methods=['post'])
def createUser():
    data = {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
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
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        return redirect('/')
    else:
        session['user_id'] = user.id
        return redirect('/')
    
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/user/animals/')
def userAnimals():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theUserAnimals = User.userAnimals(data)
        return render_template('myAnimals.html', user=theUser, userAnimals=theUserAnimals)