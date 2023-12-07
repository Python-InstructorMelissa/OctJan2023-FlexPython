from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User
from flask_app.models.image_model import Image


@app.route('/image/add/')
def addImage():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        return render_template('add_image.html', user=theUser)
    

@app.route('/image/create/', methods=['post'])
def createImage():
    theImage = Image.save(request.form)
    if not theImage:
        return redirect('/image/add/')
    else:
        return redirect('/')
    

@app.route('/image/<int:imageID>/view/')
def viewImage(imageID):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': imageID
    }
    userData = {
        'id': session['user_id']
    }
    theImage = Image.getOne(data)
    theUsers = User.getAll()
    theUser = User.getOne(userData)
    return render_template('view_image.html', user=theUser, users=theUsers, image=theImage)

@app.route('/image/<int:imageID>/edit/')
def editImage(imageID):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': imageID
    }
    userData = {
        'id': session['user_id']
    }
    theImage = Image.getOne(data)
    theUser = User.getOne(userData)
    return render_template('edit_image.html', user=theUser, image=theImage)


@app.route('/image/<int:imageID>/update/', methods=['post'])
def updateImage(imageID):
    data = {
        'id': imageID,
        'title': request.form['title']
    }
    theImage = Image.update(data)
    return redirect(f'/image/{imageID}/view/')

@app.route('/image/<int:imageID>/delete/')
def deleteImage(imageID):
    data = {
        'id': imageID
    }
    Image.delete(data)
    return redirect('/')