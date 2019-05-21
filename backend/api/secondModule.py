from bson import ObjectId

class secondAlgorithm:
    def __init__(self, skole, fakulteti, zanimanja, odabir):
        self.skole = skole
        self.fakulteti = fakulteti
        self.zanimanja = zanimanja
        self.odabir = {
            "skolaId": odabir["skolaId"],
            "zanimanjeId": odabir["zanimanjeId"]
        }


    def filter_fakulteta(self):
        odabranoZanimanjeKategorija = ""
        filtriraniFakulteti = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                odabranoZanimanjeKategorija = i["kategorija"]


        for i in self.fakulteti:
            if i["kategorija"] == odabranoZanimanjeKategorija:
                filtriraniFakulteti.append(i)
        
        return filtriraniFakulteti
    
    def usporedba_fakulteta(self):
        potrebnaZnanjaZanimanje = []
        brojPoklapanja = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                for a in i["potrebnaZnanja"]:
                    potrebnaZnanjaZanimanje.append(a["id"])
        x = set(potrebnaZnanjaZanimanje)
                    
        
        for i in self.filter_fakulteta():
            dobivenaZnanjaFakulteta = []

            for j in i["smjerovi"]:
                dobivenaZnanjaId = []

                for k in j["kolegiji"]:
                    for z in k["dobivenaZnanja"]:
                        dobivenaZnanjaId.append(z["id"])
                
                for a in dobivenaZnanjaId:
                    dobivenaZnanjaFakulteta.append(a)
                
            y = set(dobivenaZnanjaFakulteta)

            zz = list(x.intersection(y))
            brojZnanja = len(zz)

            brojPoklapanja.append({
                "idFakulteta" : i["_id"],
                "brojIstihZnanja" : brojZnanja
            })

        return brojPoklapanja

    def sortiranje_fakulteta(self):
        def sortByKey(e):
            return e["brojIstihZnanja"]

        sortiraniFakulteti = self.usporedba_fakulteta()
        sortiraniFakulteti.sort(key=sortByKey, reverse = True)

        return sortiraniFakulteti

    def izlaz(self):
        return {
            "listaFakulteta" : self.sortiranje_fakulteta(),
            "skolaId": self.odabir["skolaId"],
            "zanimanjeId": self.odabir["zanimanjeId"]
        }





            