from flask import Flask, jsonify
from flask_restful import Resource, Api
import pymongo
from bson.json_util import dumps
import requests

app = Flask(__name__)
Data_Galerias = []
Data_Multi = []
Data_VIP = []
Data_SA = []

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
    data_galerias = coleccion.find({"cine": "Galerias", "fecha": "19-marzo-2021"})
    data_multi = coleccion.find({"cine": "Multiplaza", "fecha": "19-marzo-2021"})
    data_VIP = coleccion.find({"cine": "VIP Galerias", "fecha": "19-marzo-2021"})
    data_sa = coleccion.find({"cine": "Santa Ana", "fecha": "19-marzo-2021"})

    for galerias in data_galerias:
        Data_Galerias.append(galerias)

    for multi in data_multi:
        Data_Multi.append(multi)

    for vip in data_VIP:
        Data_VIP.append(vip)

    for sa in data_sa:
        Data_SA.append(sa)

    json_data = dumps({"Galerias": Data_Galerias, "Multiplaza": Data_Multi, "VIP Galerias": Data_VIP, "Santa Ana": Data_SA})
    cliente.close()
    return json_data


def getAll():
    data_galerias = coleccion.find({"cine": "Galerias"})
    data_multi = coleccion.find({"cine": "Multiplaza"})
    data_VIP = coleccion.find({"cine": "VIP Galerias"})
    data_sa = coleccion.find({"cine": "Santa Ana"})

    for galerias in data_galerias:
        Data_Galerias.append(galerias)

    for multi in data_multi:
        Data_Multi.append(multi)

    for vip in data_VIP:
        Data_VIP.append(vip)

    for sa in data_sa:
        Data_SA.append(sa)

    json_data = dumps({"Galerias": Data_Galerias, "Multiplaza": Data_Multi, "VIP Galerias": Data_VIP, "Santa Ana": Data_SA})
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
