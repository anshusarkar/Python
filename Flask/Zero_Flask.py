from flask import Flask

app = Flask(__name__)

@app.route('/') # this decorator routes a folder as an argument, the / defualts to durrent directory 
def hello_world():
    return "<b> My first application in action ! </>"




app.run()

# It's better to add a if__name__ == '__main__' over the app.run() statement as 
# it would not let the script run if the script is imported as a 
# module.... but why would you want to import it ?

