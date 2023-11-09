from flask import Flask

app = Flask(__name__)

# The secret Key is the only thing that potentially will change on this file
app.secret_key = "Melissa is a dodo brain today"