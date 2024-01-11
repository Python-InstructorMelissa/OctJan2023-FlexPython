from flask_app import app
from flask import redirect, render_template, session, flash, request
from flask_app.models.userModel import User
from flask_app.models.gameModel import Game


@app.route('/game/add/')
def addGame():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('addGame.html', user=theUser)

@app.route('/game/create/', methods=['post'])
def createGame():
    data = request.form
    Game.save(data)
    return redirect('/')

@app.route('/game/edit/<int:game_id>/')
def editGame(game_id):
    if 'user_id' not in session:
        return redirect('/')
    pass

@app.route('/game/update/<int:game_id>/', methods=['post'])
def updateGame(game_id):
    pass

@app.route('/game/view/<int:game_id>/')
def viewGame(game_id):
    if 'user_id' not in session:
        return redirect('/')
    pass

@app.route('/game/delete/<int:game_id>/')
def deleteGame(game_id):
    pass