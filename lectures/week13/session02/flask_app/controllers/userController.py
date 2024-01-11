from flask_app import app
from flask import redirect, render_template, session, flash, request
from flask_bcrypt import Bcrypt
from flask_app.models.userModel import User
from flask_app.models.gameModel import Game

bcrypt = Bcrypt(app)


@app.route('/test/')
def testing():
    return render_template('test.html')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theGames = Game.getAll()
        theUsers = User.getAll()
        return render_template('dashboard.html', user=theUser, games=theGames, users=theUsers)
    
@app.route('/registration/', methods=['post'])
def registration():
    isvalid = User.validation(request.form)
    if not isvalid:
        return redirect('/')
    else:
        newUser = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/')
        else:
            session['user_id'] = id
            flash("Hey welcome your now a member")
            return redirect('/')


@app.route('/login/', methods=['post'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("That email is not in our system please register")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Yo dude wrong password check your spelling")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("Welcome back user")
        return redirect('/')