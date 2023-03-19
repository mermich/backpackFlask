# app.py

import json
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello_world():
    return "Hello, World!"

# Recuperation de tous les elements.
@app.route('/api/InventoryItems', methods=['GET'])
def get_InventoryItems():
    # recuperation de la connexion a la base de donnees.
    mydb = getDb()
    mycursor = mydb.cursor()

    # requete
    sql = f'SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory'

    # affichage de la requete dans la console.
    print(sql)

    # execution de la requete et recuperation des enregistrements.
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    # construction d'un objet json.
    payload = []
    content = {}
    for result in myresult:
        content = {'id': result[0], 'name': result[1], 'description': result[2], 'inTheBag': result[3]}
        payload.append(content)
        content = {}

    return jsonify(payload)

# Recuperation d'un element en particulier.
@app.route('/api/InventoryItems/<id>', methods=['GET'])
def get_InventoryItem(id):  
    sql = f'SELECT `Id`, `Name`, `Description`, `InTheBag` FROM backpack.inventory where `id`={id}'
    print(sql)
    mydb = getDb()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return jsonify(myresult)


# Creation d'un nouvel element.
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

# Modification d'un element existant.
@app.route('/api/InventoryItems', methods=['PUT'])
def update_InventoryItems():
    item = request.json
    sql = f'UPDATE Backpack.Inventory SET `Name` = "{item["name"]}", `Description` = "{item["description"]}", `InTheBag` = {item["inTheBag"]} WHERE Id = {item["id"]};'
    mydb = getDb()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204

# Suppression en base de donnees.
@app.route('/api/InventoryItems/<id>', methods=['DELETE'])
def delete_InventoryItems(id):    
    sql = f'DELETE FROM Backpack.Inventory WHERE Id = {id};'
    print(sql)
    mydb = getDb()
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    return '', 204

# Methode interne pour centraliser la connexion a la base de donnees.
def getDb():
    mydb = mysql.connector.connect(host="127.0.0.1",user="admin",password="admin",database="Backpack")
    return mydb

# Methode main de pyton apelle au lancement du fichier.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)