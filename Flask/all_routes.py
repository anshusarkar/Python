from flask import Flask, request

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    if request.method == 'GET':
        # Handle GET requests (e.g., fetch user data)
        return 'Fetching user data'
    elif request.method == 'POST':
        # Handle POST requests (e.g., create a new user)
        return 'Creating a new user'
    elif request.method == 'PUT':
        # Handle PUT requests (e.g., update an existing user)
        return 'Updating user data'
    elif request.method == 'DELETE':
        # Handle DELETE requests (e.g., delete a user)
        return 'Deleting a user' 
    
if __name__ == '__main__':
    app.run()