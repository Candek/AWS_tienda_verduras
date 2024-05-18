from flask import render_template, request, jsonify
from database.db import connectionSQL, insert_records, consult_records
from controller.s3_control import connection_s3, upload_file_s3, save_file, get_file_s3

def func_register_user():
    data_user = request.form
    photo = request.files["photo"]
    id, name, category, price = data_user["id"], data_user["name"], data_user["category"], data_user["price"]
    confirm = insert_records(id, name, category, price)
    if confirm:
        s3_connection = connection_s3()
        photo_path = save_file(id, photo)
        upload_file_s3(s3_connection, photo_path)
        return render_template("Buy.html")
    else:
        return render_template("Buy.html")
    
def func_consult_user():
    data_id = request.get_json()
    result = consult_records(data_id["id"])
    if result != None and len(result) != 0 :
        s3_connection = connection_s3()
        name_file = get_file_s3(s3_connection, data_id["id"])
        print(name_file)
        name = result[0][1]
        category = result[0][2]
        price = "1990-01-01"
        resp_data = {
            "status":"ok",
            "name":name,
            "category": category,
            "price": price,
            "photo" : name_file
        }
    else:
        resp_data = {"status":"error"}
    return jsonify(resp_data)