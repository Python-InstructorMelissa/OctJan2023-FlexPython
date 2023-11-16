from flask_app import app
from flask import render_template, redirect, session, request

# theRoot = {
#     'title': 'title',
    # 'name': 'name',
    # 'cohort': 'cohort'
# }
theUsers = []
theQuotes = []
@app.route('/')
def index():
    # global theUser
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
        theUser = {}
        uId = session['user_id']
        for u in theUsers:
            if u['id'] == uId:
                theUser = u
            else:
                theUser = {
                    'firstName': 'List Cleared'
                }
    return render_template('index.html', root=theRoot, user=theUser, quotes=theQuotes, users=theUsers)

@app.route('/success/')
def success():
    # global theUser
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
        theUser = {}
        uId = session['user_id']
        for u in theUsers:
            if u['id'] == uId:
                theUser = u
            else:
                theUser = {
                    'firstName': 'List Cleared'
                }
    print('the user',theUser, 'session', session['user_id'])
    return render_template('success.html', root=theRoot, user=theUser)

@app.route('/user/add/')
def addUser():
    # global theUser
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
    if len(theUsers) > 0:
        id = len(theUsers) +1
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
    theUsers.append(user)
    print(theUsers)
    return redirect('/')

@app.route('/clearSession/')
def clearSession():
    session.clear()
    return redirect('/')