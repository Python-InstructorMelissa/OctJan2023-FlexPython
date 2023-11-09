from flask_app import app
from flask import render_template, redirect, session, request


quotes = []
users = []

@app.route('/')
def index():
    if 'name' not in session:
        theName = 'Guest'
    else:
        theName = session['name']
    theQuotes = quotes
    theUsers = users
    print('the quotes', theQuotes, 'the users', users)
    return render_template('index.html', quotes=theQuotes, name=theName, users=theUsers)

@app.route('/quote/add/')
def addQuote():
    if 'name' not in session:
        theName = 'Guest'
    else:
        theName = session['name']
    return render_template('addQuote.html', name=theName)

@app.route('/quote/create/', methods=['POST'])
def createQuote():
    print('list length', len(users))
    data = {
        'line01': request.form['line01'],
        'line02': request.form['line02'],
        'name': request.form['name']
    }
    quotes.append(data)
    
    if len(users) > 0:
        for u in users:
            print('what is u', u)
            if u['name'] == request.form['name']:
                u['count'] = u['count'] + 1
            else:
                userData = {
                    'name': request.form['name'],
                    'count': 1
                }
                users.append(userData)    
    else:
        userData = {
            'name': request.form['name'],
            'count': 1
        }
        users.append(userData)
    newUser = request.form['name']
    session['name'] = newUser
    print('the quotes', quotes)
    return redirect('/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')