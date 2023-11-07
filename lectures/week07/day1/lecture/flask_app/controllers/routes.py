from flask_app import app
from flask import render_template, redirect, session, request

# theRoot = {
#     'title': 'title',
    # 'name': 'name',
    # 'cohort': 'cohort'
# }
squishies = []

@app.route('/')
def index():
    theRoot = {
        'title': 'Forms and Session',
        'name': 'Melissa',
        'cohort': 'Oct-Feb Cohort'
    }
    if 'name' not in session:
        session['name'] = 'Guest'
    theSquishies = squishies
    print('the list', squishies)
    return render_template('index.html', root=theRoot, name = session['name'], squishies=theSquishies)

@app.route('/addSquish/', methods=['post'])
def addSquish():
    session['name'] = request.form['name']
    oneSquishy = {
        'name': request.form['name'],
        'img': request.form['img']
    }
    squishies.append(oneSquishy)
    return redirect('/success/')

@app.route('/clearSession/')
def clearSession():
    session.clear()
    return redirect('/')


@app.route('/success/')
def success():
    theRoot = {
        'title': 'Forms and Session',
        'name': 'Melissa',
        'cohort': 'Oct-Feb Cohort'
    }
    if 'name' not in session:
        session['name'] = 'Guest'
    return render_template('success.html', root=theRoot, name = session['name'])