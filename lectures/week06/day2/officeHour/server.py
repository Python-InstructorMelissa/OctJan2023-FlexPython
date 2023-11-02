from flask import Flask


app = Flask(__name__)


@app.route('/')
#  / is always the root route.  Where the site will open to by default
def index():
    return "I am a string on the root route"

@app.route('/classroom/')
def classroom():
    return "Hey welcome to the class!!!!!! I am so glad that you are here today"

@app.route('/classroom/<int:num>/')
def classroomNum(num):
    return f"Welcome to class #{num}!"

@app.route('/classroom/math/<int:numA>/<int:numB>/')
def classroomMath(numA, numB):
    if numA > 10:
        adding = numA + numB
        return f"Welcome to math today we are adding {numA} + {numB} and we should get {adding}"
    if numA <= 10:
        square = numA * numA
        adding = numA + numA
        return f"Welcome to math.  Today we are both adding and looking at exponents {numA} squared = {square}.  But Adding {numA} + {numA} will give you {adding}"

@app.route('/classroom/<subject>/')
def classroomSubject(subject):
    return f"Welcome to {subject}.  Glad you could make it"




if __name__ == "__main__":
    app.run(debug=True)


"""
The Environment is like the utilities that we get hooked up to our home.  On their own they don't do anything but they are there ready to be used.
When we turn on the server it's like wiring up an outlet to the power box and plugging in a lamp now we have things that it can do we just then need to call them.
The lamp route when activated will then turn the lamp on but it can't turn on unless power is applied 1st to the house and then 2nd routed to the lamp properly
"""