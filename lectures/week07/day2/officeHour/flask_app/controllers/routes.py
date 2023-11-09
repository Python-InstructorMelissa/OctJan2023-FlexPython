from flask_app import app
from flask import render_template, redirect, session, request

# theRoot = {
#     'title': 'title',
    # 'name': 'name',
    # 'cohort': 'cohort'
# }
users = []
quotes = []
@app.route('/')
def index():
    global theUser
    theRoot = {
        'title': 'title',
        'name': 'name',
        'cohort': 'cohort'
    }
    if 'user_id' not in session:
        theUser = {
    'firstName': 'Guest'
    }
    else:
        aUser = session['user_id']
        for u in users:
            if u['id'] == aUser:
                theUser = u
    return render_template('index.html', root=theRoot, user=theUser)

@app.route('/success/')
def success():
    global theUser
    theRoot = {
        'title': 'title',
        'name': 'name',
        'cohort': 'cohort'
    }
    if 'user_id' not in session:
        theUser = {
    'firstName': 'Guest'
    }
        return redirect('/user/add/')
    else:
        aUser = session['user_id']
        for u in users:
            if u['id'] == aUser:
                theUser = u
    print('the user',theUser, 'session', session['user_id'])
    return render_template('index.html', root=theRoot, user=theUser)

@app.route('/user/add/')
def addUser():
    global theUser
    theRoot = {
        'title': 'title',
        'name': 'name',
        'cohort': 'cohort'
    }
    if 'user_id' not in session:
        theUser = {
            'firstName': 'Guest'
        }
    else:
        return redirect('/success/')
    return render_template('logReg.html', root=theRoot, user=theUser)

@app.route('/user/create/', methods=['POST'])
def createUser():
    if len(users) > 0:
        id = len(users) +1
    else:
        id = 1
    user = {
        'id': id,
        'username': request.form['username'],
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'password': request.form['password']
    }
    newUser = user['id']
    session['user_id'] = newUser
    users.append(user)
    print(users)
    return redirect('/')