class Aufgabe:
    def __init__(self):
        self.HOTELS = []
        self.bewertungMinimum = 0
        self.maximaleLaenge = 360
        self.strecke = 1510
        self.loesung = []

    def _getMoeglicheStrecken(self, letztesVerwendetesHotel):
        moeglicheStrecken = [] 

        """

            Bedingte Anweisung, die alle Hotels rausfiltert, die sich
            innerhalb 360 Längeneinheiten des letzten verwendeten Hotels
            befindet.
            Die erste Abfrage dient zum filtern des Bereichs auf innerhalb
            360 Längeneinheiten, der zweite Bereich sorgt dafür, dass man
            nicht zurückfährt oder zu einem Hotel der gleichen Entfernung fährt.
            In dem Fall lohnt es sich nicht zurück zufahren um ein Hotel zu besuchen
            dass hinter Einem liegt, weil man das Hotel, dass Hinter einem liegt
            zuerst besuchen könnte aber auch, da die perfekte Strecke 5 * 260 1800 ergibt,
            und man mit einer Zurückfahrt oder das Bleiben im Hotel für maximale Ideale Strecke von 1540 liefert,
            welche in 4/5 Beispielen übertroffen wird. 
            Das Wechseln in ein Hotel mit der selben Entfernung, aber unterschiedlicher
            Bewertung macht ebenfalls kein Sinn, da man nur das Hotel mit der besseren Bewertung
            besuchen könnte und das andere Ignorieren.

        """

        for hotel in self.HOTELS:
            if hotel[0] - letztesVerwendetesHotel[0] <= self.maximaleLaenge and \
               hotel[0] - letztesVerwendetesHotel[0] > 0:
                moeglicheStrecken.append(hotel)

        return moeglicheStrecken

    def _getSchlechtesteBewertung(self, strecke):
        """

            6 als Wert der nicht durch Bewertungen erreicht werden kann. 
            Theoretisch kann jeder Wert über 5 für diese Variable
            verwendet werden.

        """

        schlechtesteBewertung = 6

        for hotel in strecke:
            if hotel[1] < schlechtesteBewertung:
                schlechtesteBewertung = hotel[1]
        
        return schlechtesteBewertung

    # def _sortiere_nach_bester():

    def _amEnde(self, letztesVerwendetesHotel):
        if (self.strecke - letztesVerwendetesHotel[0]) <= self.maximaleLaenge:
            return True
        
        return False

    def _loesen(self, letztesVerwendetesHotel, loesungsStrecke):
        """

            Optimierung: Falls eine Strecke über 4 Hotels enthält, kann 
            mithilfe der Rückgabe der Vorgang abgebrochen werden, weil
            somit das Ziel nicht innerhalb 5 Tage erreicht wird. 
            Außerdem wird abgebrochen, wenn es nicht mehr möglich ist 
            die restliche Strecke, innerhalb der verbleibenden Tage und pro
            Tag 6 Fahrstunden, zu überqueren

        """

        if len(loesungsStrecke) > 4 or ( len(loesungsStrecke) != 0 and \
            self.strecke - loesungsStrecke[-1][0] > (5 - len(loesungsStrecke)) * self.maximaleLaenge):
            return

        """
        
            Die Methode _getMoeglicheStrecken gibt alle Strecken zurück
            die ab dem letzten verwendeten Hotels möglich sind, innerhalb 
            der 6 Stunden Grenze

        """

        moeglicheStrecken = self._getMoeglicheStrecken(letztesVerwendetesHotel)

        """

            Falls eine komplette Strecke gefunden wurde, 
            vergleiche die schlechteste Bewertung dieser mit der
            bewertungMinimum Variable und ersetze diese, falls die 
            schlechteste Bewertung besser ist

        """

        if len(moeglicheStrecken) == 0 or self._amEnde(letztesVerwendetesHotel):
            schlechtesteBewertung = self._getSchlechtesteBewertung(loesungsStrecke)

            if self.bewertungMinimum < schlechtesteBewertung:
                self.bewertungMinimum = schlechtesteBewertung
                #print(loesungsStrecke, self.bewertungMinimum)
                self.loesung = loesungsStrecke[:]
            return

        # Für optimierung: sorten nach bester bewertung

        for strecke in moeglicheStrecken:

            """

                Falls eine Strecke mit einem Hotel ausgewählt wird,
                wessen bewertung schon unter der mindes Bewertung einer
                anderen Strecke ausgewählt wird, wird diese Strecke 
                übersprungen

            """
            if strecke[1] < self.bewertungMinimum:
                continue
            
            """

                Strecke wird hier rekursiv aufgebaut und nach jedem
                rekursivem Durchlauf wieder an den Anfangszustand gebracht,
                damit die nächste Strecke in der nächsten Iteration verwendet
                werden kann.

            """
            loesungsStrecke.append(strecke)
            self._loesen(strecke, loesungsStrecke)
            loesungsStrecke.pop()

    def _readInput(self, file):
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

    def _formatierLoesung(self, loesungsweg):
        if self.strecke > loesungsweg[-1][0] + self.maximaleLaenge:
            print("Das Ziel kann nicht erreicht werden, da die Distanz zwischen den Hotels zu groß ist.")
            return

        print("Die geeigneteste Strecke nach den Kriterien ist:")
        for [ stop, hotel ] in loesungsweg:
            print(f"- Stop bei {stop} für das Hotel mit der Bewertung {hotel}")


        print(f"Die schlechteste Bewertung der Hotels ist {self._getSchlechtesteBewertung(loesungsweg)}")
 
    
    def main(self, file):
        self._readInput(file)
        self._loesen( [0, 0], [] )
        self._formatierLoesung(self.loesung)



test = Aufgabe()
test.main("hotels7.txt")