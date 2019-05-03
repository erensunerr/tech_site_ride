from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    pass #TODO: create template for index page

@app.route('/products')
def products():
    pass #TODO: code this

@app.route('/legal')
def legal():
    pass #TODO: code this

@app.route('/buy')
def buy():
    pass #TODO: code this

#GENERAL TODO: Code a rest api to retrieve reservation info, create a db for reservation info.

