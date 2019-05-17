from flask import Flask
from flask_pymongo import PyMongo
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mc2"
mongo = PyMongo(app)


class Person:
    def __init__(self, skole, fakulteti, zanimanja, odabir):
        self.skole = skole
        self.fakulteti = fakulteti
        self.zanimanja = zanimanja
        self.odabir = {
            "skolaId": odabir["skolaId"],
            "fakultetId": odabir["fakultetId"],
            "smjerId": odabir["smjerId"],
            "zanimanjeId": odabir["zanimanjeId"]
        }

    def dohvacanjePodataka(self):
        skola = {}
        fakultet = {}
        zanimanje = {}
        
        for i in self.skole:
            if str(i["_id"]) == self.odabir["skolaId"]:
                skola = i

        for i in self.fakulteti:
            if str(i["_id"]) == self.odabir["fakultetId"]:
                fakultet = i

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                zanimanje = i

        return {
            "skola": skola,
            "fakultet": fakultet,
            "zanimanje": zanimanje
        }
    
    def generiranje_znanja(self):
        potrebnaZnanjaZanimanje = []
        dobivenaZnanjaFakultet = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                for a in i["potrebnaZnanja"]:
                    potrebnaZnanjaZanimanje.append(a["id"])
                

        for j in self.fakulteti:
            if str(j["_id"]) == self.odabir["fakultetId"]:
                for b in j["smjerovi"]:
                    if str(b["id"]) == self.odabir["smjerId"]:
                        for c in b["predmeti"]:
                            for d in c["dobivenaZnanja"]:
                                dobivenaZnanjaFakultet.append(d["id"])
                
        return potrebnaZnanjaZanimanje, dobivenaZnanjaFakultet

    def usporedba_znanja(self):
        x, y = self.generiranje_znanja()
        potrebnaZnanjaZanimanje = set(x)
        dobivenaZnanjaFakultet = set(y)

        korisnaDobivenaZnanja = potrebnaZnanjaZanimanje.intersection(dobivenaZnanjaFakultet)
        filtriranaPotrebnaZnanja = potrebnaZnanjaZanimanje.difference(dobivenaZnanjaFakultet)

        return {
            "korisnaDobivenaZnanja": list(korisnaDobivenaZnanja),
            "filtriranaPotrebnaZnanja": list(filtriranaPotrebnaZnanja)
        } 
    

    def izlaz(self):
        def odaberiSmjer(id):
            for i in self.dohvacanjePodataka()["fakultet"]["smjerovi"]:
                if str(i["id"]) == self.odabir["smjerId"]:
                    return i

        izlazniObjekt = {
            "_id": ObjectId(),
            "userId": "",
            "skola": {
                "skolaId": self.odabir["skolaId"],
                "naziv": self.dohvacanjePodataka()["skola"]["naziv"],
                "korisnaDobivenaZnanja": [],
                "preporucenaZnanja": []
            },
            "fakultet": {
                "fakultetId": self.odabir["fakultetId"],
                "naziv": self.dohvacanjePodataka()["fakultet"]["naziv"],
                "korisnaDobivenaZnanja": self.usporedba_znanja()["korisnaDobivenaZnanja"],
                "preporucenaZnanja": self.usporedba_znanja()["filtriranaPotrebnaZnanja"],
                "upis": odaberiSmjer(id)["upis"]
            },
            "zanimanje": {
                "zanimanjeId": self.odabir["zanimanjeId"],
                "zaposljavanje": {
                    "tvrtke": [],
                    "ustanove": []
                },
                "minimalnaRazinaObrazovanja": self.dohvacanjePodataka()["zanimanje"]["minimalnaRazinaObrazovanja"],
                "preporucenaZnanja": []
            },
            "interesi": []
        }

        return izlazniObjekt
        
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
    "interesi" : []
}
p1 = Person(skole, fakulteti, zanimanja, osoba1)

@app.route('/')
def hello():
    return JSONEncoder().encode(p1.izlaz())
    