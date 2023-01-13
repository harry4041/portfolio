from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    email = request.form['email']
    return render_template('index.html', variable = email)