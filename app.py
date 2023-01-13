from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup():
    email = request.form['SUemail']
    password = request.form['SUpassword']

    return render_template('index.html', email = email, password = password)





