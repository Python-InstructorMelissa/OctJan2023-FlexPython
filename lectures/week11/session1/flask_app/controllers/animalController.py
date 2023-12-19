from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models.userModel import User
from flask_app.models.animalModel import Animal



@app.route('/animal/add/')
def addAnimal():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addAnimal.html', user=theUser)

@app.route('/animal/create/', methods=['post'])
def createAnimal():
    theAnimal =  Animal.save(request.form)
    return redirect('/')