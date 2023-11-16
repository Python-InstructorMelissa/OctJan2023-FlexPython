from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.herbModel import herbs
from flask_app.models.locationModel import locations
from flask_app.models.potionModel import potions
from flask_app.models.outcomeModel import outcomes
import random
from datetime import datetime

current = datetime.now()

theEssence = 0
theActivities = []
theGathered = []

@app.route('/')
def index():
    thePotions = potions
    theHerbs = herbs
    theLocations = locations
    theOutcomes = outcomes
    if 'lastAction' not in session:
        theAction = "None"
    else:
        theAction = session['lastAction']
    return render_template('index.html', essence=theEssence, activities=theActivities, herbs=theHerbs, locations=theLocations, potions=thePotions, outcomes=theOutcomes, action=theAction)

@app.route('/gather/')
def gatherHerbs():
    global theEssence
    selection = random.choice(herbs)
    print('random herb', selection)
    points = selection['essence_points']
    print('points', points)
    theEssence += points
    activity = f"{selection['name']} was gathered from {selection['location']} at {current} and {points} points were added to the total Essence Points"
    session['lastAction'] = activity
    theActivities.append(activity)
    theGathered.append(selection['name'])
    return redirect('/')

@app.route('/potion/')
def chosePotion():
    global theGathered
    global theEssence
    selection = random.choice(potions)
    points = selection['essence_points']
    theEssence += points
    activity = f"{selection['name']} was created at {current} and {points} points were added to the total Essence Points"
    session['lastAction'] = activity
    theActivities.append(activity)
    return redirect('/')


@app.route('/outcome/')
def theOutcome():
    global theGathered
    global theEssence
    selection = random.choice(outcomes)
    points = selection['essence_points']
    theEssence += points
    activity = f"At {current}, {points} points were added to the total Essence Points because there was a {selection['name']}"
    session['lastAction'] = activity
    theActivities.append(activity)
    return redirect('/')