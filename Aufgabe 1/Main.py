

ersterInput = input().split()
visualisierung = "|"
ersteReihe = ""
outputs = []
for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ersteReihe+=x
    outputs.append("")
    if(x==ersterInput[1]):
        break
visualisierung+=ersteReihe
visualisierung=" "+(len(visualisierung)-1)*"-"+"\n"+visualisierung+"|"
visualisierung+="\n"+visualisierung.split("\n")[1]+"\n"+" "

letztePosition = -2
schiebeReihe = ""
for x in range(int(input(""))):
    zweiterInput = input("").split()
    schiebeReihe +=  " "*(int(zweiterInput[1])-(letztePosition+2))+2*zweiterInput[0] 
    visualisierung+=" "*(int(zweiterInput[1])-(letztePosition+2))+2*zweiterInput[0] 
    letztePosition = int(zweiterInput[1])
schiebeReihe+= " "*(len(ersteReihe)-len(schiebeReihe))
print(visualisierung)
#print(schiebeReihe)




def schieben(richtung, spalte):
    if(richtung == "rechts"):
        range_ = range(spalte, len(ersteReihe), 1)
    else:
        range_ = range(spalte, -1, -1)
    if(schiebeReihe[range_[1]]==schiebeReihe[spalte]):
        platz = 1
    else:
        platz = 2
    letztesAuto = "1"
    autoAnzahl = 0
    verschiebungsAnzahl = 0
    output = ""
    for x in range_:
        if(schiebeReihe[x]==" "):
            platz-=1
        else:
            if(schiebeReihe[x]!=letztesAuto):
                output = schiebeReihe[x]+" "+str(platz)+" "+richtung + ", " + output
                autoAnzahl+=1
                verschiebungsAnzahl+=platz
                letztesAuto = schiebeReihe[x]
        if(platz==0):
            break
    if(platz!=0):
        return -1
    else:
        output = output[:-2]
        output = ersteReihe[spalte]+": "+output
        print(richtung+": Autoanzahl-"+str(autoAnzahl)+" Verschiebungsanzahl-"+str(verschiebungsAnzahl))
        if(richtung == "links"):
            outputs[spalte]= output 
            global linksVerschiebungsAnzahl 
            linksVerschiebungsAnzahl = verschiebungsAnzahl
        else:
            if(autoAnzahl<linksAutoAnzahl or linksAutoAnzahl==-1 or (autoAnzahl==linksAutoAnzahl and verschiebungsAnzahl<linksVerschiebungsAnzahl)):
               outputs[spalte]= output  
        return autoAnzahl

for spalte in range(len(ersteReihe)):
    #überprüfen ob unten blockiert
    print("--")
    if(schiebeReihe[spalte]==" "):
        outputs[spalte] = ersteReihe[spalte]+":"
    else:
        linksVerschiebungsAnzahl = -1
        if(spalte!=0):
            linksAutoAnzahl = schieben("links", spalte)
        else:
            linksAutoAnzahl = -1
        if(spalte != len(ersteReihe)-1):
            schieben("rechts", spalte)
    print("--")




print(outputs)
for output in outputs:
    print(output)