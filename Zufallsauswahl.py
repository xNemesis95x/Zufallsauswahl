import random

def Zufallsauswahl ():
    while True:
        erneut_Ausfuehren = input ("Was möchten sie machen geben sie bitte die entsprechende Zahl ein? \n1. Das Programm ausführen um eine Liste zu erstellen \n2. Das Programm beenden\n")
        if erneut_Ausfuehren == "1":
            Auswahlliste = []
            while True:
                weitere_Eintraege = input ("Was möchten Sie machen geben sie bitte die entsprechende Zahl ein? \n1. Einen Eintrag der Liste hinzufügen \n2. Einen zufälligen Eintrag aus der Liste auswählen lassen. \n")

                if weitere_Eintraege == "1":
                    Eintrag = input ("Bitte den entsprechenden Eintrag eingeben: \n")
                    Auswahlliste.append (Eintrag)

                elif weitere_Eintraege == "2":
                    zufaellige_Auswahl = random.choice (Auswahlliste)
                    print ("Ihr Ergebnis ist: ", zufaellige_Auswahl)
                    break

        elif erneut_Ausfuehren == "2":
            break

Zufallsauswahl ()