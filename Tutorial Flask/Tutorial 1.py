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

@app.route('/main')
def hi() : 
    return '1234'
@app.route('/f')
def test() :
    return render_template('index.html')
if __name__ == '__main__' :
    app.run(debug= True)