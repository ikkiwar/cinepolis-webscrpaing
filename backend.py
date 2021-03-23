from flask import Flask
from flask_restful import Resource, Api
import pymongo
from bson.json_util import dumps
import requests

app = Flask(__name__)
Data = []

#Conexion a la base de datos
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 1000
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
MONGO_BASEDATOS = "prueba"
MONGO_COLECCION = "cine"

cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_BASEDATOS]
coleccion = baseDatos[MONGO_COLECCION]


def getFecha():
    data = coleccion.find({"fecha": "19-marzo-2021"})
    for r in data:
        Data.append(r)
    json_data = dumps(Data)
    cliente.close()
    return json_data


def getAll():
    data = coleccion.find()
    for r in data:
        Data.append(r)
    json_data = dumps(Data)
    cliente.close()
    return json_data


@app.route("/")
def index():
    return "Web Scraping Cinepolis"


@app.route("/getFecha/")
def get_fecha():
    return getFecha()


@app.route("/getAll/")
def get_all():
    return getAll()


if __name__ == "__main__":
    app.run(debug=True)
