class Aufgabe:
    def __init__(self):
        self.HOTELS = []
        self.bewertung_minimum = 0
        self.maximale_laenge = 360
        self.strecke = 1510

    def _get_moegliche_strecken(self, letztes_verwendetes_hotel):
        moegliche_strecken = [] 

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
            if hotel[0] - letztes_verwendetes_hotel[0] <= self.maximale_laenge and \
               hotel[0] - letztes_verwendetes_hotel[0] > 0:
                moegliche_strecken.append(hotel)

        return moegliche_strecken

    def _get_schlechteste_bewertung(self, strecke):
        """

            6 als Wert der nicht durch Bewertungen erreicht werden kann. 
            Theoretisch kann jeder Wert über 5 für diese Variable
            verwendet werden.

        """

        schlechteste_bewertung = 6

        for hotel in strecke:
            if hotel[1] < schlechteste_bewertung:
                schlechteste_bewertung = hotel[1]
        
        return schlechteste_bewertung

    # def _sortiere_nach_bester():

    def _am_ende(self, letztes_verwendetes_hotel):
        if (self.strecke - letztes_verwendetes_hotel[0]) <= self.maximale_laenge:
            return True
        
        return False

    def _loesen(self, letztes_verwendetes_hotel, loesungs_strecke):
        """

            Optimierung: Falls eine Strecke über 4 Hotels enthält, kann 
            mithilfe der Rückgabe der Vorgang abgebrochen werden, weil
            somit das Ziel nicht innerhalb 5 Tage erreicht wird. 
            Außerdem wird abgebrochen, wenn es nicht mehr möglich ist 
            die restliche Strecke, innerhalb der verbleibenden Tage und pro
            Tag 6 Fahrstunden, zu überqueren

        """

        if len(loesungs_strecke) > 4 or ( len(loesungs_strecke) != 0 and \
            self.strecke - loesungs_strecke[-1][0] > (5 - len(loesungs_strecke)) * self.maximale_laenge):
            return

        """
        
            Die Methode _get_moegliche_strecken gibt alle Strecken zurück
            die ab dem letzten verwendeten Hotels möglich sind, innerhalb 
            der 6 Stunden Grenze

        """

        moegliche_strecken = self._get_moegliche_strecken(letztes_verwendetes_hotel)

        """

            Falls eine komplette Strecke gefunden wurde, 
            vergleiche die schlechteste Bewertung dieser mit der
            bewertung_minimum Variable und ersetze diese, falls die 
            schlechteste Bewertung besser ist

        """

        if len(moegliche_strecken) == 0 or self._am_ende(letztes_verwendetes_hotel):
            schlechteste_bewertung = self._get_schlechteste_bewertung(loesungs_strecke)

            if self.bewertung_minimum < schlechteste_bewertung:
                self.bewertung_minimum = schlechteste_bewertung
                print(loesungs_strecke, self.bewertung_minimum)

            return

        # Für optimierung: sorten nach bester bewertung

        for strecke in moegliche_strecken:

            """

                Falls eine Strecke mit einem Hotel ausgewählt wird,
                wessen bewertung schon unter der mindes Bewertung einer
                anderen Strecke ausgewählt wird, wird diese Strecke 
                übersprungen

            """
            if strecke[1] < self.bewertung_minimum:
                continue
            
            """

                Strecke wird hier rekursiv aufgebaut und nach jedem
                rekursivem Durchlauf wieder an den Anfangszustand gebracht,
                damit die nächste Strecke in der nächsten Iteration verwendet
                werden kann.

            """
            loesungs_strecke.append(strecke)
            self._loesen(strecke, loesungs_strecke)
            loesungs_strecke.pop()

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
        self.read_input(file)

        loesungs_strecke = []
        self._loesen( [0, 0], loesungs_strecke)



test = Aufgabe()
test.main("hotels5.txt")