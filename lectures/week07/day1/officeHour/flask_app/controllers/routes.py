from flask_app import app
from flask import render_template
from flask_app.dataFiles import mealPlanning



# theRoot = {
#     'title': 'title',
    # 'name': 'name',
    # 'cohort': 'cohort'
# }
@app.route('/')
def index():
    theRoot = {
        'title': 'Meal Planning',
        'name': 'The Class',
        'cohort': 'The Best Oct-Feb Cohort'
    }
    thePresent = [
        'Anthony',
        'Kevin',
        'Robert',
        'Melissa'
    ]
    theInfo = [
        {
        'device': "Mac OS",
        'age': 45,
        'geek': True,
        'spouse': 'Nick'
        },
        {
        'device': "Windows 11",
        'age': 36,
        'geek': False,
        'spouse': 'Anthony'
        }
    ]
    return render_template('index.html', root=theRoot, present=thePresent, info=theInfo)