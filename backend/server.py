from flask import Flask, request, Response
from flask_pymongo import PyMongo
import json
from bson import ObjectId
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

def konverzija(kolekcija):
    lista = []
    for x in kolekcija.find():
        lista.append(x)
    return lista

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config["MONGO_URI"] = "mongodb://localhost:27017/mc2Unos"
mongo = PyMongo(app)

@app.route('/fakulteti')
def dohvatiFakultete():
    fakulteti = konverzija(mongo.db.fakultets)
    fakulteti = JSONEncoder().response(fakulteti)
    return fakulteti

@app.route('/skole')
def dohvatiSkole():
    skole = konverzija(mongo.db.skolas)
    skole = JSONEncoder().response(skole)
    return skole

@app.route('/zanimanja')
def dohvatiZanimanja():
    zanimanja = konverzija(mongo.db.zanimanjes)
    zanimanja = JSONEncoder().response(zanimanja)
    return zanimanja

@app.route('/getstepdata', methods = ['POST'])
def sendStepData():
    req = request.get_json(force=True)
    skolaID = req['highSchool']
    fakultetID = req['college']
    zanimanjeID = req['profession']
    
    skola = mongo.db.skolas.find_one({"_id" : ObjectId(skolaID)})
    fakultet = mongo.db.fakultets.find_one({"_id" : ObjectId(fakultetID)})
    # zanimanje = mongo.db.zanimanjes.find_one({"_id" : zanimanjeID})

    res = {
        "highSchool" : skola,
        "college" : fakultet,
        "profession" : ""
    }

    return JSONEncoder().response(res)