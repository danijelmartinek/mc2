from flask import Flask, request, Response
from flask_pymongo import PyMongo
import json
from bson import ObjectId

from api.mainModule import mainAlgorithm
from api.secondModule import secondAlgorithm
from api.thirdModule import thirdAlgorithm
import datetime
from flask_cors import CORS

import time


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

@app.route('/fakulteti')
def dohvatiFakultete():
    fakultetiLista = JSONEncoder().response(fakulteti)
    return fakultetiLista

@app.route('/skole')
def dohvatiSkole():
    skoleLista = JSONEncoder().response(skole)
    return skoleLista

@app.route('/zanimanja')
def dohvatiZanimanja():
    zanimanjaLista = JSONEncoder().response(zanimanja)
    return zanimanjaLista

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

@app.route('/gencaseone', methods = ['POST'])
def generiranjePutova1():
    req = request.get_json(force=True)
    res = mainAlgorithm(skole, fakulteti, zanimanja, req).izlaz()
    return JSONEncoder().response([res])

@app.route('/gencasetwo', methods = ['POST'])
def generiranjePutova2():
    req = request.get_json(force=True)
    listaPuteva = []
    odgovarajuciFakulteti = secondAlgorithm(skole, fakulteti, zanimanja, req).izlaz()

    for i in odgovarajuciFakulteti['listaFakulteta']:
        put = mainAlgorithm(skole, fakulteti, zanimanja, {
            'fakultetId' : i['idFakulteta'],
            'skolaId' : odgovarajuciFakulteti['skolaId'],
            'zanimanjeId' : odgovarajuciFakulteti['zanimanjeId']
             }).izlaz()
        
        listaPuteva.append(put)

    return JSONEncoder().response(listaPuteva)

@app.route('/gencasethree', methods = ['POST'])
def generiranjePutova3():
    req = request.get_json(force=True)
    listaPuteva = []
    odgovarajucaZanimanja = thirdAlgorithm(skole, fakulteti, zanimanja, req).izlaz()

    for i in odgovarajucaZanimanja['listaZanimanja']:
        put = mainAlgorithm(skole, fakulteti, zanimanja, {
            'fakultetId' : odgovarajucaZanimanja['fakultetId'],
            'skolaId' : odgovarajucaZanimanja['skolaId'],
            'zanimanjeId' : i['idZanimanja']
             }).izlaz()
        
        listaPuteva.append(put)

    return JSONEncoder().response(listaPuteva)