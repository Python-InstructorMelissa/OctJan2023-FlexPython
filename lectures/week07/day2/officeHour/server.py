from flask_app import app
# This file remains the same other than the controller file imports
from flask_app.controllers import routes


if __name__ == "__main__":
    app.run(debug=True)