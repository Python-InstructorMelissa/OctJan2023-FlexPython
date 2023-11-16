from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.gardenModel import herb_gardens_data
from flask_app.models.herbModel import herbs_data
from flask_app.models.userModel import users_data

theRoot = {
    'title': '',
    'footer': ''
}


@app.route('/')
def index():
    theRoot = {
        'title': 'Mystical Garden App',
        'footer': 'Thanks for growing with us'
    }
    theUsers = users_data
    return render_template('index.html', root=theRoot, users=theUsers)

@app.route('/user/add/')
def addUser():
    theRoot = {
        'title': 'Mystical Garden App',
        'footer': 'Thanks for growing with us'
    }
    theUsers = users_data
    return render_template('addUser.html', root=theRoot, users=theUsers)

@app.route('/user/create/', methods=['post'])
def createUser():
    theUsers = len(users_data)
    theUsers += 1
    data = {
        'id': theUsers,
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }
    users_data.append(data)
    print('the form data', data, 'new list', users_data)
    return redirect('/')

@app.route('/user/<id>/view/')
def viewUser(id):
    theRoot = {
        'title': 'Mystical Garden App',
        'footer': 'Thanks for growing with us'
    }
    userId = id
    aUser = {}
    for user in users_data:
        print('the ids', user['id'], 'the user', user)
        if user['id'] == userId:
            print('got inside if')
            aUser = user
    print('the url id', userId, 'the matched user', aUser)
    theUser = aUser
    return render_template('viewUser.html', root=theRoot, user=theUser)