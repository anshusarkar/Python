from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def sample_template():
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(debug=True)
