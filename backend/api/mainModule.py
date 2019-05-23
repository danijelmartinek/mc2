from bson import ObjectId

class mainAlgorithm:
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
                    if str(b["id"]) == self.odabir["smjerId"]:
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
                "korisnaDobivenaZnanja": self.usporedba_znanja_skola()["korisnaDobivenaZnanja"],
                "preporucenaZnanja": []
            },
            "fakultet": {
                "fakultetId": self.odabir["fakultetId"],
                "naziv": self.dohvacanjePodataka()["fakultet"]["naziv"],
                "korisnaDobivenaZnanja": self.usporedba_znanja_fakultet()["korisnaDobivenaZnanja"],
                "preporucenaZnanja": [],
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