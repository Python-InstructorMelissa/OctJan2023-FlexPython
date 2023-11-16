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

# @app.route('/quote/create/', methods=['POST'])
# def createQuote():
#     print('list length', len(users))
#     data = {
#         'line01': request.form['line01'],
#         'line02': request.form['line02'],
#         'name': request.form['name']
#     }
#     quotes.append(data) # Take quote data add to quote list
    
#     if len(users) > 0: # if user list not empty
#         for u in users: # loop through users
#             print('what is u', u)
#             if u['name'] == request.form['name']: # if the form user name == iteration user name
#                 u['count'] = u['count'] + 1 # take iteration user count increase by 1
#             else: # if user not found
#                 userData = {
#                     'name': request.form['name'],
#                     'count': 1
#                 }
#                 users.append(userData)    # add user to list with a count of 1
#     else: # if list is empty 
#         userData = {
#             'name': request.form['name'],
#             'count': 1
#         }
#         users.append(userData) # add user to list with count of 1
#     newUser = request.form['name'] # take form name set to newUser
#     session['name'] = newUser # put new user into session
#     print('the quotes', quotes)
#     return redirect('/')

# in python empty list and dicts =  False (js = True)

@app.route('/quote/create/', methods=['POST'])
def createQuote():
    quotes.append(request.form)
    found = False
    for user in users:
        if user['name'] == request.form['name']:
            user['count'] += 1
            found = True
    if not found: users.append({'name': request.form['name'], 'count': 1})
    session['name'] =  request.form['name']
    return redirect('/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')