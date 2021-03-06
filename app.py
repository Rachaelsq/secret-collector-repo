from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import sys
from send_email import send_email

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
    secret_ = db.Column(db.String(800), unique=True)

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
        #send email
        send_email(email, secret)
        #query the database model (Data) and filter to show when the value of email is not unique, will not show success but keep on index.html
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            
            #create object instance of data class
            data=Data(email, secret)
            #commit new row/changes to database
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
        return render_template('index.html',
        text="That email has been used already")




''' 
==================
Run
==================
'''
if __name__ =='__main__':
    app.debug=True
    app.run()