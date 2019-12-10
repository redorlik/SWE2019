from flask import Flask

app = Flask(__name__)


# Creates the URL route
@app.route('/')
# Defines function for this route which will be executed
def index1():
    # returns a string to the webpage
    return "Hello from flask"


# main program
if __name__ == '__main__':
    # Flask run command, initiates flask in debug mode and defines host.
    app.run(debug=True, host='0.0.0.0')
