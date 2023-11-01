from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route('/')   # The "@" decorator associates this route with the function immediately following
def helloFlask():
    return 'Welcome to Flask everyone!'   # Return the string 'Hello World!' as a response

@app.route('/anthonysRoom/')
def anthonysRoom():
    return "Unless you are Anthony Get out of here"


@app.route('/room1/<int:num>/')   # <int:num> means that this route requires and integer in the place of this <> to work  in this case it is called num
def room1(num): # the integer requested buy the route was called num so this function take a parameter of that integer to work
    return f"Welcome to Room 1 our capacity is {num}"  # and then fills that integer into where {num} is


@app.route('/room2/<name>/')
def room2(name):
    return f"Welcome to Room 2, other wise known as {name}'s Room"



if __name__ == "__main__":  # Ensure this file is being run directly and not from a different module  
    app.run(debug=True)   # Run the app in debug mode.