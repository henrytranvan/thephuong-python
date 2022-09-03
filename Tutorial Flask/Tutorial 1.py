from pydoc import render_doc
from re import template
from string import Template
from flask import Flask
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort


app = Flask(__name__)

@app.route('/')
def hi() : 
    return render_template('home.html')

@app.route('/login', methods = ['POST','GET']) 
def login() :
    if request.method == "POST" :
        USN = request.form['USname']
        if name :
            return redirect(url_for('hello_user', name = USN))
    return render_template('loginpage.html')

@app.route('/hi/<name>') 
def hello_user(name):
    return f'<a>Hello {name}</a>'

if __name__ == '__main__' :
    app.run(debug= True)
