from flask import Flask 

app = Flask("My FIRST Application") # Here goes the app name

@app.route('/')

def hello():
    return "Hello, World!"

app.run(debug=True)