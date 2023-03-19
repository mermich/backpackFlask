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
  mydb = getDb()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory")
  myresult = mycursor.fetchall()
  return jsonify(myresult)

@app.route('/api/InventoryItems/<id>', methods=['GET'])
def get_InventoryItem(id):
  mydb = getDb()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory where `id`="+id)
  myresult = mycursor.fetchall()
  return jsonify(myresult)


@app.route('/api/InventoryItems', methods=['POST'])
def add_InventoryItems():
    item = request.json
    sql = f'INSERT INTO Backpack.Inventory (Name, Description, InTheBag) VALUES ("{item["name"]}", "{item["description"]}", {item["inTheBag"]});'
    print(sql)
    mydb = getDb()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204


@app.route('/api/InventoryItems', methods=['PUT'])
def update_InventoryItems():
    item = request.json
    sql = f'UPDATE Backpack.Inventory SET `Name` = "{item["name"]}", `Description` = "{item["description"]}", `InTheBag` = {item["inTheBag"]} WHERE Id = {item["id"]};'
    mydb = getDb()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204

@app.route('/api/InventoryItems/<id>', methods=['DELETE'])
def delete_InventoryItems(id):
    mydb = getDb()
    sql = f'DELETE FROM Backpack.Inventory WHERE Id = {id};'
    print(sql)
    mycursor = db.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204


def getDb():
   mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
   return mydb

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)