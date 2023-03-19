# app.py

import json
import mysql.connector
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/api/InventoryItems', methods=['GET'])
def get_InventoryItems():
  mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
  mycursor = mydb.cursor()
  mycursor.execute("SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory")
  myresult = mycursor.fetchall()
  return jsonify(myresult)

@app.route('/api/InventoryItems/<id>', methods=['GET'])
def get_InventoryItem(id):
  mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
  mycursor = mydb.cursor()
  mycursor.execute("SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory where `id`="+id)
  myresult = mycursor.fetchall()
  return jsonify(myresult)


@app.route('/api/InventoryItems', methods=['POST'])
def add_InventoryItems():
    item = request.json
    mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
    sql = f'INSERT INTO Backpack.Inventory (Name, Description, InTheBag) VALUES ("{item["name"]}", "{item["description"]}", {item["inTheBag"]});'
    print(sql)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204


@app.route('/api/InventoryItems', methods=['PUT'])
def update_InventoryItems():
    item = request.json
    mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
    sql = f'UPDATE Backpack.Inventory SET `Name` = "{item["name"]}", `Description` = "{item["description"]}", `InTheBag` = {item["inTheBag"]} WHERE Id = {item["id"]};'
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204

@app.route('/api/InventoryItems/<id>', methods=['DELETE'])
def delete_InventoryItems(id):
    mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
    sql = f'DELETE FROM Backpack.Inventory WHERE Id = {id};'
    print(sql)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)