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


    #metoda generira listu fakulteta uzimajući u obzir kategoriju zadanog zanimanja
    def filter_fakulteta(self):
        odabranoZanimanjeKategorija = ""
        filtriraniFakulteti = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                odabranoZanimanjeKategorija = i["kategorija"]


        for i in self.fakulteti:
            for j in i['smjerovi']:
                if j["kategorija"] == odabranoZanimanjeKategorija:
                    if i not in filtriraniFakulteti:
                        filtriraniFakulteti.append(i)
        
        return filtriraniFakulteti
    

    #usporedba izlaznih znanja svakog filtiranog fakulteta s potrebnim znanjima za zanimanje
    def usporedba_fakulteta(self):
        potrebnaZnanjaZanimanje = []
        brojPoklapanja = []

        for i in self.zanimanja:
            if str(i["_id"]) == self.odabir["zanimanjeId"]:
                for a in i["potrebnaZnanja"]:
                    potrebnaZnanjaZanimanje.append(a["_id"])
        x = set(potrebnaZnanjaZanimanje)
                    
        
        for i in self.filter_fakulteta():
            dobivenaZnanjaFakulteta = []

            for j in i["smjerovi"]:
                dobivenaZnanjaId = []

                for k in j["kolegiji"]:
                    for z in k["dobivenaZnanja"]:
                        dobivenaZnanjaId.append(z["_id"])
                
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


    #sortiranje fakulteta po broju znanja koja se preklapaju sa znanjima odabranog zanimanja
    def sortiranje_fakulteta(self):
        def sortByKey(e):
            return e["brojIstihZnanja"]

        sortiraniFakulteti = self.usporedba_fakulteta()
        sortiraniFakulteti.sort(key=sortByKey, reverse = True)

        return sortiraniFakulteti


    #izlazni objekt/riječnik
    def izlaz(self):
        return {
            "listaFakulteta" : self.sortiranje_fakulteta(),
            "skolaId": self.odabir["skolaId"],
            "zanimanjeId": self.odabir["zanimanjeId"]
        }





            