from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="mysql+mysqlconnector://root:@localhost/SIH"

db = SQLAlchemy(app) 

class Login(db.Model):
    table_name='login'
    Sno=db.Column(db.Integer,primary_key=True)
    Username=db.Column(db.String(80),nullable=False)
    Email=db.Column(db.String(80),nullable=False)
    Password=db.Column(db.String(150),nullable=False) 
    Date=db.Column(db.String(80),nullable=True)
  


@app.route("/")
def main():
    return render_template("index.html")

@app.route('/register',methods=["GET","POST"])
def reg():
    if request.method=="post":
        usr=request.form.get("username")
        email=request.form.get("email")
        passw=request.form.get("pswd")
        entry=Login(Username=usr,Email=email,Password=passw,Date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return redirect('/dashboard')

    return render_template("form.html")


@app.route('/login')
def login():
    return render_template("form.html")

if(__name__=="__main__"):
    Flask.run(app,debug=True)