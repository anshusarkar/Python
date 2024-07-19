from flask import Flask, render_template, request 

app = Flask("Rendering HTML templates")

@app.route('/') # This means routing all th files in the directory 
def sample_template():
    return render_template('sample.html')

# @app.route('/user/anshu', methods=['GET']) a get method syncs data from frontend where a post method sends data to frontend 
# def getUser(username):
#     return render_template('inout.html', username=username)

# @app.route('user', methods=['GET'])
# def getUserBasedOnReq():
#     username = request.args.get('username')
#     return render_template('result.html', username=username)

if __name__ == '__main__':
    app.run(debug = True, port = 5550)