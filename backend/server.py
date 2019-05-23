from flask import Flask
from flask_pymongo import PyMongo
import json
from bson import ObjectId
from api.mainModule import mainAlgorithm
from api.secondModule import secondAlgorithm
from api.thirdModule import thirdAlgorithm

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mc2"
mongo = PyMongo(app)

  
def konverzija(kolekcija):
    lista = []
    for x in kolekcija.find():
        lista.append(x)
    return lista

skole = konverzija(mongo.db.skole)
fakulteti = konverzija(mongo.db.fakulteti)
zanimanja = konverzija(mongo.db.zanimanja)          
osoba1 = {
    "fakultetId": "5cdec1dde96cf85787949292",
    "smjerId": "5cdec1dde96cf85787949293",
    "skolaId": "5cdebf15f88a0c5529953b7d",
    "zanimanjeId": "bf63bdd35bfea107408f28e1",
    "interesi": []
}
p1 = mainAlgorithm(skole, fakulteti, zanimanja, osoba1)
p2 = secondAlgorithm(skole, fakulteti, zanimanja, osoba1)
p3 = thirdAlgorithm(skole, fakulteti, zanimanja, osoba1)

@app.route('/')
def hello():
    return JSONEncoder().encode(p3.izlaz())
    