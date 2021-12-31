from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import sys

app=Flask(__name__)
#postgres database url
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/secret_collector'
db=SQLAlchemy(app)


''' 
================
MODEL
================
'''
class Data(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    secret_ = db.Column(db.String)

    def __init__(self, email_, secret_):
        self.email_=email_
        self.secret=secret_



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
        #create object instance of data class
        data=Data(email, secret)
        #commit new row/changes to database
        db.session.add(data)
        db.session.commit()
    return render_template("success.html")




''' 
==================
Run
==================
'''
if __name__ =='__main__':
    app.debug=True
    app.run()