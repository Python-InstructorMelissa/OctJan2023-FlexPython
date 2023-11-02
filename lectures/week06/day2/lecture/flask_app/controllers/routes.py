from flask_app import app
from flask import render_template, redirect
from flask_app.dataFiles.parkAnimals import *

# theRoot = {
#     'title': 'title',
# }

@app.route('/')
def index():
    theRoot = {
        'title': 'Parks & Animals'
    }
    return render_template('index.html', root=theRoot)

@app.route('/fakeData/')
def fakeData():
    theRoot = {
        'title': 'Parks & Animals'
    }
    theParks = parkAnimals
    return render_template('fakeData.html', root=theRoot, parks=theParks)

@app.route('/animal/<int:id>/')
def oneAnimal(id):
    theRoot = {
        'title': 'Parks & Animals'
    }
    for park in parkAnimals:
        print('park in loop', park)
        for animal in park['animals']:
            theAnimal = animal
    print(theAnimal)
    return render_template('oneAnimal.html', root=theRoot, animal=theAnimal)
