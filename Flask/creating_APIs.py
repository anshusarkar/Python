from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({'message': 'Hello, my guy!'})


if __name__ == '__main__':
    app.run(debug=True)
    
# now use "curl http://127.0.0.1:5000" to read the API msg .
# now use "curl http://127.0.0.1:5000\hello" to read the API msg .