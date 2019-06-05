from flask import Flask, request, Response, session
from flask_pymongo import PyMongo
from flask_cors import CORS
import json
from bson import ObjectId
import datetime
import time


from api.mainModule import mainAlgorithm
from api.secondModule import secondAlgorithm
from api.thirdModule import thirdAlgorithm

from api.auth import Auth, SignUp




class JSONEncoder(json.JSONEncoder):  #klasa za pretvorbu Mongo objekata u string
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


uSession = Auth(app)
uSession.init(3600)


@app.route('/register', methods = ['POST'])
def userRegister():
    data = request.get_json(force=True)
    registeredUser = SignUp(uSession, mongo.db.commonUsers).registerUser(data)
    res = JSONEncoder().response(registeredUser)

    return res

@app.route('/login', methods = ['POST'])
def userLogin():
    data = request.get_json(force=True)
    loggedUser = SignUp(uSession, mongo.db.commonUsers).loginUser(data)
    res = JSONEncoder().response(loggedUser)

    return res

@app.route('/logout')
def clear():
    return uSession.clearSession()

@app.route('/checksession')
def checkSession():
    return uSession.getSession()

  


















def konverzija(kolekcija):  #vraća listu s traženim objektima iz baze podataka
    lista = []
    for x in kolekcija.find():
        lista.append(x)
    return lista

skole = konverzija(mongo.db.skole)
fakulteti = konverzija(mongo.db.fakulteti)
zanimanja = konverzija(mongo.db.zanimanja)



# glavne rute za generiranje puteva
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



#ruta za preuzimanje podataka vezanih za generiranu rutu
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



#ostale rute za preuzimanje podataka
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



