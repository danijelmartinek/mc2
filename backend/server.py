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
            "skola": odabir["skola"],
            "fakultet": odabir["fakultet"],
            "zanimanje": odabir["zanimanje"]
        }
    
    def generiranje_znanja(self):
        potrebnaZnanjaZanimanje = []
        dobivenaZnanjaFakultet = []

        for i in self.zanimanja:
            if i["naziv"] == self.odabir["zanimanje"]:
                potrebnaZnanjaZanimanje = i["potrebnaZnanja"]

        for i in self.fakulteti:
            if i["naziv"] == self.odabir["fakultet"]:
                listaZnanja = [] 
                for a in i["predmeti"]:
                    for b in a["dobivenaZnanja"]:
                        listaZnanja.append(b)
                dobivenaZnanjaFakultet = listaZnanja

        return potrebnaZnanjaZanimanje, dobivenaZnanjaFakultet
    
    def usporedba_znanja(self):
        
        x, y = self.generiranje_znanja()
        potrebnaZnanjaZanimanje = set(x)
        dobivenaZnanjaFakultet = set(y)
        return list(potrebnaZnanjaZanimanje - dobivenaZnanjaFakultet), list(dobivenaZnanjaFakultet - potrebnaZnanjaZanimanje) 
        
        


def konverzija(kolekcija):
    lista = []
    for x in kolekcija.find():
        lista.append(x)
    return lista

skole = konverzija(mongo.db.skole)
fakulteti = konverzija(mongo.db.fakulteti)
zanimanja = konverzija(mongo.db.zanimanja)          
osoba1 = {
    "fakultet": "TVZ",
    "skola": "gimnazija",
    "zanimanje": "zanimanje1",
    "interesi" : []
}
p1 = Person(skole, fakulteti, zanimanja, osoba1)

@app.route('/')
def hello():
    return JSONEncoder().encode(p1.usporedba_znanja())
    