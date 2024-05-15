from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', methods=['GET']) # the app.route method defualts to get method 
def hello_world():
    return send_file("Html/Homepage.html")
  


if __name__ == '__main__':
    app.run()