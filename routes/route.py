from flask import render_template, request, jsonify
from servidor import app
from database.db import connectionSQL, insert_records, consult_records

@app.route('/')
def home_page():
   connectionSQL()
   return render_template("Market.html") 
   
@app.route('/Buy')   
def register_page():
    return render_template("Buy.html") 
    
@app.route('/Sell')   
def consult_page():
    return render_template("Sell.html") 
    
@app.route('/register_user', methods=["post"])   
def register_user():
    data_user = request.form
    id, name, category, price = data_user["id"], data_user["name"], data_user["category"], data_user["price"]
    insert_records(id, name, category, price)
    return render_template("Buy.html")
    
@app.route('/consult_user', methods=["post"]) 
def consult_user():
    data_id = request.get_json()
    result = consult_records(data_id["id"])
    if result != None and len(result) != 0 :
        name = result[0][1]
        category = result[0][2]
        price = "1990-01-01"
        resp_data = {"status":"ok",
            "name":name,
            "category": category,
            "price": price
        }
    else:
        resp_data = {"status":"error"}
    print(result)
    return jsonify(resp_data)
    
    