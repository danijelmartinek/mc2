from flask import Flask, request, Response
from flask_pymongo import PyMongo
import json
from bson import ObjectId
from api.mainModule import mainAlgorithm
from api.secondModule import secondAlgorithm
from api.thirdModule import thirdAlgorithm
import datetime
from flask_cors import CORS

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.timedelta):
            return (datetime.datetime.min + o).time().isoformat()
        else:
            return json.JSONEncoder.default(self, o)
    def response(self, obj):
        return Response(self.encode(obj), mimetype='application/json')


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

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

@app.route('/fakulteti')
def dohvatiFakultete():
    fakulteti = JSONEncoder().response(fakulteti)
    return fakulteti

@app.route('/skole')
def dohvatiSkole():
    skole = JSONEncoder().response(skole)
    return skole

@app.route('/zanimanja')
def dohvatiZanimanja():
    zanimanja = JSONEncoder().response(zanimanja)
    return zanimanja

@app.route('/getstepdata', methods = ['POST'])
def sendStepData():
    req = request.get_json(force=True)
    skolaID = req['highSchool']
    fakultetID = req['college']
    zanimanjeID = req['profession']
    
    skola = mongo.db.skole.find_one({"_id" : ObjectId(skolaID)})
    fakultet = mongo.db.fakulteti.find_one({"_id" : ObjectId(fakultetID)})
    zanimanje = mongo.db.zanimanja.find_one({"_id" : ObjectId(zanimanjeID)})

    res = {
        "highSchool" : skola,
        "college" : fakultet,
        "profession" : zanimanje
    }

    return JSONEncoder().response(res)
    