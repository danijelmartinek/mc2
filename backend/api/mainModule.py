from bson import ObjectId

class mainAlgorithm:
    def __init__(self, skole, fakulteti, zanimanja, odabir):
        self.skole = skole
        self.fakulteti = fakulteti
        self.zanimanja = zanimanja
        self.odabir = {
            "skolaId": str(odabir["skolaId"]),
            "fakultetId": str(odabir["fakultetId"]),
            "zanimanjeId": str(odabir["zanimanjeId"])
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

        print(self.odabir["fakultetId"])

        return {
            "skola": skola,
            "fakultet": fakultet,
            "zanimanje": zanimanje
        }
    
    def generiranje_znanja_fakultet(self):
        potrebnaZnanjaZanimanje = []
        dobivenaZnanjaFakultet = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                for a in i["potrebnaZnanja"]:
                    potrebnaZnanjaZanimanje.append(a["id"])
                

        for j in self.fakulteti:
            if str(j["_id"]) == self.odabir["fakultetId"]:
                for b in j["smjerovi"]:
                    for c in b["kolegiji"]:
                        for d in c["dobivenaZnanja"]:
                            dobivenaZnanjaFakultet.append(d["id"])
                
        return potrebnaZnanjaZanimanje, dobivenaZnanjaFakultet

    def generiranje_znanja_skola(self):
        potrebnaZnanjaZanimanje = self.usporedba_znanja_fakultet()["filtriranaPotrebnaZnanja"]
        dobivenaZnanjaSkola = []

        for j in self.skole:
            if str(j["_id"]) == self.odabir["skolaId"]:
                for c in j["predmeti"]:
                    for d in c["dobivenaZnanja"]:
                        dobivenaZnanjaSkola.append(d["id"])
                
        return potrebnaZnanjaZanimanje, dobivenaZnanjaSkola

    def usporedba_znanja_fakultet(self):
        x, y = self.generiranje_znanja_fakultet()
        potrebnaZnanjaZanimanje = set(x)
        dobivenaZnanjaFakultet = set(y)

        korisnaDobivenaZnanja = potrebnaZnanjaZanimanje.intersection(dobivenaZnanjaFakultet)
        filtriranaPotrebnaZnanja = potrebnaZnanjaZanimanje.difference(dobivenaZnanjaFakultet)

        return {
            "korisnaDobivenaZnanja": list(korisnaDobivenaZnanja),
            "filtriranaPotrebnaZnanja": list(filtriranaPotrebnaZnanja)
        }
    
    def usporedba_znanja_skola(self):
        x, y = self.generiranje_znanja_skola()
        potrebnaZnanjaZanimanje = set(x)
        dobivenaZnanjaSkola = set(y)

        korisnaDobivenaZnanja = potrebnaZnanjaZanimanje.intersection(dobivenaZnanjaSkola)
        filtriranaPotrebnaZnanja = potrebnaZnanjaZanimanje.difference(dobivenaZnanjaSkola)

        return {
            "korisnaDobivenaZnanja": list(korisnaDobivenaZnanja),
            "filtriranaPotrebnaZnanja": list(filtriranaPotrebnaZnanja)
        } 
    

    def izlaz(self):
        
        izlazniObjekt = {
            "_id": ObjectId(),
            "userId": "",
            "skola": {
                "skolaId": self.odabir["skolaId"],
                "naziv": self.dohvacanjePodataka()["skola"]["naziv"],
                "korisnaDobivenaZnanja": self.usporedba_znanja_skola()["korisnaDobivenaZnanja"],
                "preporucenaZnanja": []
            },
            "fakultet": {
                "fakultetId": self.odabir["fakultetId"],
                "naziv": self.dohvacanjePodataka()["fakultet"]["naziv"],
                "korisnaDobivenaZnanja": self.usporedba_znanja_fakultet()["korisnaDobivenaZnanja"],
                "preporucenaZnanja": [],
            },
            "zanimanje": {
                "zanimanjeId": self.odabir["zanimanjeId"],
                "naziv": self.dohvacanjePodataka()["zanimanje"]["naziv"],
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