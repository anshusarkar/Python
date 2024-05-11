from flask import Flask

app = Flask(__name__)

@app.route('/') # This decorator takes 
def hello_world():
    return "<b> My first application in action ! </>"

app.run()
