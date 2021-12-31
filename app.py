from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import sys

app=Flask(__name__)


''' 
==================
Routes
==================
'''
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success', methods=['POST'])
def success():
#if the user initiates a post request in order to get to success.html, return success
    if request.method=='POST':
        email=request.form["email_name"]
        secret=request.form["secret_text"]
        print(request.form)
    return render_template("success.html")




''' 
==================
Run
==================
'''
if __name__ =='__main__':
    app.debug=True
    app.run()