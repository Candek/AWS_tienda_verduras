from flask import render_template, request
from servidor import app
from controller.control import func_register_user, func_consult_user

@app.route('/')
def home_page():
   return render_template("Market.html") 
   
@app.route('/Buy')   
def register_page():
    return render_template("Buy.html") 
    
@app.route('/Sell')   
def consult_page():
    return render_template("Sell.html") 
    
@app.route('/register_user', methods=["post"])   
def register_user():
    return func_register_user()
    
@app.route('/consult_user', methods=["post"]) 
def consult_user():
    return func_consult_user()
    
    