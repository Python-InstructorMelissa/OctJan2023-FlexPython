from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.ownerModel import Owner

@app.route('/test')
def testing():
    return render_template('index.html')

@app.route('/logout/')
def logout():
    session.clear()
    flash('Keep the change you filthy animal!')
    return redirect('/')


@app.route('/')
def index():
    if 'owner' in session:
        theOwner = session['owner']
    else:
        theOwner = False
    return render_template('index.html', owner=theOwner)


# if the static method is_valid returns any of the if statements as is_valid = False then the flash message will be used to print on the webpage the error you encountered however it will only last for that singular redirect.
@app.route('/create/owner/', methods=['post'])
def createOwner():
    is_valid = Owner.validation(request.form)
    if not is_valid: 
        flash("not good man")
        return redirect('/')
    else :
        flash("Good Job")
        session['owner'] = request.form['first_name']
        return redirect('/')
