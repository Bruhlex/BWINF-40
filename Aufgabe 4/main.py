import sys
sys.setrecursionlimit(10000)

import random
class Aufgabe:
    def __init__(self):
        self.WUERFEL = []
        self.SPIELER_STATUS = {}

    def _setSpieler(self, spieler1, wuerfel1, spieler2, wuerfel2):
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

        self.SPIELER_STATUS[spieler1]["WUERFEL"] = wuerfel1
        self.SPIELER_STATUS[spieler2]["WUERFEL"] = wuerfel2

    def _getErgebnis(self, wuerfel):
        return random.choice(wuerfel)

    def _getIndex(self, list, value):
        return list.index(value)

    def _checkGegenspieler(self, indexOfSpieler, amZug, naechsterZug): 
        """

            Check ob sich ein Gegenspieler auf dem Feld befindet das man betreten will.
            Falls ja, wird der Gegenspieler zurück auf das B-Feld gestoßten und man selbst
            schreitet auf das Feld hinauf
            
        """
                    
        spielerStats = self.SPIELER_STATUS[amZug]
        gegenSpielerStats = self.SPIELER_STATUS[naechsterZug]

        positionGegenspieler = spielerStats["POSITIONEN"][indexOfSpieler] + 20
        positionGegenspieler2 = spielerStats["POSITIONEN"][indexOfSpieler] - 20
        if positionGegenspieler in gegenSpielerStats["POSITIONEN"]:
            gegenSpielerStats["POSITIONEN"][self._getIndex(gegenSpielerStats["POSITIONEN"], positionGegenspieler)] = 0
            gegenSpielerStats["B-FELD"] += 1

        if positionGegenspieler2 in gegenSpielerStats["POSITIONEN"]:
            gegenSpielerStats["POSITIONEN"][self._getIndex(gegenSpielerStats["POSITIONEN"], positionGegenspieler2)] = 0
            gegenSpielerStats["B-FELD"] += 1

    def _simulierSpiel(self, startSpieler):
        amZug = startSpieler

        while True:
            if amZug == "schwarz":
                naechsterZug = "gruen"
            else:
                naechsterZug = "schwarz"

            # Spiel spiel bis gewinner
            spielerStats = self.SPIELER_STATUS[amZug]
            wuerfelWert = self._getErgebnis(spielerStats["WUERFEL"])

            #  check if winner

            """

                Falls es noch Spieler im B Feld gibt und es keine gleichen Spieler
                sich auf dem selben Feld befinden, dann bekommt ein B Feld Spieler
                die Position 1

            """

            if wuerfelWert == 6 and 0 in spielerStats["POSITIONEN"]:
                if 1 not in spielerStats["POSITIONEN"]:
                    spielerStats["B-FELD"] -= 1
                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], 0)
                    spielerStats["POSITIONEN"][indexOfSpieler] = 1
                else:
                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], 1)
                    spielerStats["POSITIONEN"][indexOfSpieler] += wuerfelWert
                
                #self._checkGegenspieler(indexOfSpieler, amZug, naechsterZug)
            else:
                positionen = sorted(spielerStats["POSITIONEN"][:], reverse=True)

                for i in range(len(positionen)):
                    if  positionen[i] == 0 or positionen[i] == -1 or \
                        wuerfelWert > spielerStats["LAST_POSITION"] - positionen[i] or \
                        positionen[i] + wuerfelWert in spielerStats["POSITIONEN"]:
                        continue

                    indexOfSpieler = self._getIndex(spielerStats["POSITIONEN"], positionen[i])
                    spielerStats["POSITIONEN"][indexOfSpieler] += wuerfelWert

                    self._checkGegenspieler(indexOfSpieler, amZug, naechsterZug)

                    break

                while spielerStats["LAST_POSITION"] in spielerStats["POSITIONEN"]:
                    spielerStats["POSITIONEN"][self._getIndex(spielerStats["POSITIONEN"], spielerStats["LAST_POSITION"])] = -1
                    spielerStats["LAST_POSITION"] -= 1

            if wuerfelWert == 6:
                return self._simulierSpiel(amZug)

            if max(spielerStats["POSITIONEN"]) == -1:
                return amZug

            amZug = naechsterZug

    def _readInput(self, file):
        f = open("Aufgabe 4/assets/" + file, "r")
        content = f.read()
        f.close()

        data = content.splitlines()

        for i in range(0, len(data)):
            if(i == 0):
                continue
            else:
                wuerfel = data[i].split(" ")
                if len(wuerfel) != 0:
                    self.WUERFEL.append(list(map(int, data[i].split(" "))))
        
    def _berechneWahrscheinlichkeiten(self, durchlaeufe):
        Gewinner = [0] * len(self.WUERFEL)
        for _ in range(durchlaeufe):
            for index in range(len(self.WUERFEL)):
                wuerfel = self.WUERFEL[index]
                for index2 in range(len(self.WUERFEL)):
                    wuerfel2 = self.WUERFEL[index2]
                    if 6 not in wuerfel and 6 not in wuerfel2 or (1 not in wuerfel and 1 not in wuerfel2):
                        continue

                    for i in range(2):
                        if i == 0:
                            spieler = "schwarz"
                            gegenSpieler = "gruen"
                        elif i == 1:
                            spieler = "gruen"
                            gegenSpieler = "schwarz"

                        self._setSpieler(spieler, wuerfel, gegenSpieler, wuerfel2)
                        gewinner = self._simulierSpiel("schwarz")

                        if gewinner == spieler:
                            Gewinner[index] += 1
                        elif gewinner == gegenSpieler:
                            Gewinner[index2] += 1
                
        self._formatierLoesung(Gewinner)

    def _formatierLoesung(self, wahrscheinlichkeiten):
        spielAnzahl = sum(wahrscheinlichkeiten)
        meisteSiege = max(wahrscheinlichkeiten)
        wuerfelMeisteSiege = self.WUERFEL[wahrscheinlichkeiten.index(meisteSiege)]

        print("Für Mensch ärgere dich empfiehlt sich von den gegebenen Wuerfeln dieser Wuerfel am meisten:")
        print(wuerfelMeisteSiege)
        print(f"Dieser Wuerfel hat von {spielAnzahl} Spielen, {meisteSiege} gewonnen. Das ist eine Sieges Wahrscheinlichkeit von {round((meisteSiege/spielAnzahl)*100, 2)}%")
        print(f"Die Wahrscheinlichkeitsverteilung ist: {wahrscheinlichkeiten}")

    def main(self, file):
        self._readInput(file)
        self._berechneWahrscheinlichkeiten(20)



test = Aufgabe()
test.main("wuerfel4.txt")