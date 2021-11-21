gewichte = []
gewichteAnzahl = []
linkeGewichte = []
rechteGewichte = []

for x in range(int(input(""))):
    gewichtInput = input("").split()
    gewichte.append(int(gewichtInput[0]))
    gewichteAnzahl.append(int(gewichtInput[1]))
    linkeGewichte.append(0)
    rechteGewichte.append(0)



def linksHinlegen(messGewicht, aktGewichtIndex, aktLinkesGewicht):
    for aktGewichtAnzahl in range(gewichteAnzahl[aktGewichtIndex]+1):
        linkeGewichte[aktGewichtIndex] = aktGewichtAnzahl
        aktLinkesGewicht+= aktGewichtAnzahl * gewichte[aktGewichtIndex]
        #print(linkeGewichte)
        if(aktGewichtIndex == len(gewichte)-1):
            besterUnterschied = rechtsHinlegen(messGewicht, 0, aktLinkesGewicht, 0, 1000000)
            if(besterUnterschied == 0):
                print("Passt!: Links-"+str(linkeGewichte)+" Rechts-"+str(rechteGewichte))
        else:
            linksHinlegen(messGewicht, aktGewichtIndex+1, aktLinkesGewicht)
            aktLinkesGewicht-= aktGewichtAnzahl * gewichte[aktGewichtIndex]

def rechtsHinlegen(messGewicht, aktGewichtIndex, aktLinkesGewicht, aktRechtesGewicht, besterUnterschied):
    for aktGewichtAnzahl in range(gewichteAnzahl[aktGewichtIndex]-linkeGewichte[aktGewichtIndex]+1):
        rechteGewichte[aktGewichtIndex] = aktGewichtAnzahl
        aktRechtesGewicht+= aktGewichtAnzahl * gewichte[aktGewichtIndex]
        if(aktGewichtIndex==len(gewichte)-1 and besterUnterschied > aktLinkesGewicht - aktRechtesGewicht + messGewicht):
            #print("Links-"+str(linkeGewichte)+" Rechts-"+str(rechteGewichte))
            besterUnterschied = aktLinkesGewicht - aktRechtesGewicht + messGewicht
            if(besterUnterschied == 0):
              print("Passt!: Links-"+str(linkeGewichte)+" Rechts-"+str(rechteGewichte))  
        else:
            besterUnterschied_ = rechtsHinlegen(messGewicht, aktGewichtIndex+1, aktLinkesGewicht, aktRechtesGewicht, 1000000)
            if(besterUnterschied>besterUnterschied_):
                besterUnterschied = besterUnterschied_
            aktRechtesGewicht-= aktGewichtAnzahl * gewichte[aktGewichtIndex]
    return besterUnterschied

linksHinlegen(440, 0, 0)