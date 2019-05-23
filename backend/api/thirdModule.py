from bson import ObjectId

class thirdAlgorithm:
    def __init__(self, skole, fakulteti, zanimanja, odabir):
        self.skole = skole
        self.fakulteti = fakulteti
        self.zanimanja = zanimanja
        self.odabir = {
            "skolaId": odabir["skolaId"],
            "fakultetId": odabir["fakultetId"]
        }
    def filter_zanimanja(self):
        odabraniFakultetKategorija = ""
        filtriranaZanimanja = []

        for i in self.fakulteti:
            if str(i["_id"]) == self.odabir["fakultetId"]:
                odabraniFakultetKategorija = i["kategorija"]


        for i in self.zanimanja:
            if i["kategorija"] == odabraniFakultetKategorija:
                filtriranaZanimanja.append(i)
        
        return filtriranaZanimanja

    def usporedba_zanimanja(self):
        dobivenaZnanjaFakulteta = []
        brojPoklapanja = []

        for i in self.fakulteti:
            if str(i["_id"]) == self.odabir["fakultetId"]:
                for a in i["smjerovi"]:
                    for b in a["kolegiji"]:
                        for c in b["dobivenaZnanja"]:
                            dobivenaZnanjaFakulteta.append(c["id"])
        x = set(dobivenaZnanjaFakulteta)            
        
        for i in self.filter_zanimanja():
            potrebnaZnanjaZanimanje = []

            for j in i["potrebnaZnanja"]:
                potrebnaZnanjaZanimanje.append(j["id"])
                
            y = set(potrebnaZnanjaZanimanje)

            zz = list(x.intersection(y))
            brojZnanja = len(zz)

            brojPoklapanja.append({
                "idZanimanja" : i["_id"],
                "brojIstihZnanja" : brojZnanja
            })

        return brojPoklapanja
    
    def sortiranje_zanimanja(self):
        def sortByKey(e):
            return e["brojIstihZnanja"]

        sortiranaZanimanja = self.usporedba_zanimanja()
        sortiranaZanimanja.sort(key=sortByKey, reverse = True)

        return sortiranaZanimanja
    
    def izlaz(self):
        return {
            "listaZanimanja" : self.sortiranje_zanimanja(),
            "skolaId": self.odabir["skolaId"],
            "fakultetId": self.odabir["fakultetId"]
        }