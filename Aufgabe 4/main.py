import random

WUERFEL = [
    [ 6, 1, 2, 3, 4, 5, 6 ],
    [ 6, 1, 1, 1, 6, 6, 6 ],
    [ 4, 1, 2, 3, 4 ],
    [ 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
    [ 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ],
    [ 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ],
]

class Aufgabe:
    def __init__(self):
        self.SPIELER_STATUS = {
            "schwarz":  {
                "B-FELD"        : 4,
                "WUERFEL"       : [],
                "POSITIONEN"    : [0] * 4,
                "LAST_POSITION" : 44
            },
            "gruen":    {
                "B-FELD"        : 4,
                "WUERFEL"       : [],
                "POSITIONEN"    : [0] * 4,
                "LAST_POSITION" : 44
            }
        }

    def _setSpieler(self):
        self.SPIELER_STATUS = {
            "schwarz":  {
                "B-FELD"        : 4,
                "WUERFEL"       : [],
                "POSITIONEN"    : [0] * 4,
                "LAST_POSITION" : 44
            },
            "gruen":    {
                "B-FELD"        : 4,
                "WUERFEL"       : [],
                "POSITIONEN"    : [0] * 4,
                "LAST_POSITION" : 44
            }
        }

        self.SPIELER_STATUS["schwarz"]["WUERFEL"] = WUERFEL[0]
        self.SPIELER_STATUS["gruen"]["WUERFEL"] = WUERFEL[5]

    def _getErgebnis(self, wuerfel):
        return random.choice(wuerfel)

    def _getIndex(self, list, value):
        return list.index(value)

    def _simulierSpiel(self, startSpieler):
        amZug = startSpieler

        while True:
            if amZug == "schwarz":
                naechsterZug = "gruen"
            else:
                naechsterZug = "schwarz"

            # Spiel spiel bis gewinner
            spielerStats = self.SPIELER_STATUS[amZug]
            gegenSpielerStats = self.SPIELER_STATUS[naechsterZug]
            wuerfelWert = self._getErgebnis(spielerStats["WUERFEL"])

            #  check if winner

            """

                Falls es noch Spieler im B Feld gibt und es keine gleichen Spieler
                sich auf dem selben Feld befinden, dann bekommt ein B Feld Spieler
                die Position 1

            """
            print("Loop hier", spielerStats["B-FELD"], wuerfelWert, spielerStats["LAST_POSITION"], amZug, spielerStats["B-FELD"], spielerStats["POSITIONEN"])
            if wuerfelWert == 6 and 0 in spielerStats["POSITIONEN"]:
                if 1 not in spielerStats["POSITIONEN"]:
                    spielerStats["B-FELD"] -= 1
                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], 0)
                    spielerStats["POSITIONEN"][indexOfSpieler] = 1
                else:
                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], 1)
                    spielerStats["POSITIONEN"][indexOfSpieler] += wuerfelWert

            else:
                positionen = sorted(spielerStats["POSITIONEN"][:], reverse=True)

                for i in range(len(positionen)):
                    if positionen[i] == 0 or positionen[i] == -1 or wuerfelWert > spielerStats["LAST_POSITION"] - positionen[i] or positionen[i] + wuerfelWert in spielerStats["POSITIONEN"]:
                        continue

                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], positionen[i])
                    spielerStats["POSITIONEN"][indexOfSpieler] += wuerfelWert

                    positionGegenspieler = spielerStats["POSITIONEN"][indexOfSpieler] + 20
                    if positionGegenspieler in gegenSpielerStats["POSITIONEN"]:
                        gegenSpielerStats["POSITIONEN"][self._getIndex(gegenSpielerStats["POSITIONEN"], positionGegenspieler)] = 0
                        gegenSpielerStats["B-FELD"] += 1

                    break

                while spielerStats["LAST_POSITION"] in spielerStats["POSITIONEN"]:
                    spielerStats["POSITIONEN"][self._getIndex(spielerStats["POSITIONEN"], spielerStats["LAST_POSITION"])] = -1
                    spielerStats["LAST_POSITION"] -= 1

            if wuerfelWert == 6:
                return self._simulierSpiel(amZug)

            if max(spielerStats["POSITIONEN"]) == -1:
                return amZug

            amZug = naechsterZug

        return gewinner

    def read_input(self, file):
        f = open("Aufgabe 2/assets/" + file, "r")
        content = f.read()
        f.close()

        data = content.splitlines()

        for i in range(0, len(data)):
            if(i == 0):
                continue
            elif(i == 1):
                self.strecke = int(data[1])
            else:
                [ strecke, bewertung ] = data[i].split(" ")
                self.HOTELS.append([ int(strecke), float(bewertung) ])
        
    def main(self, file):
        #self.read_input(file)

        #loesungs_strecke = []
        self._setSpieler()
        print(self._simulierSpiel("schwarz"))



test = Aufgabe()
test.main("hotels5.txt")