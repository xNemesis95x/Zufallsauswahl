import random
from tkinter import *

def Zufallsauswahl():
    for widget in fenster.winfo_children ():
        widget.destroy ()

    # Neue Widgets nur nach Button-Klick erstellen
    global Zufallsauswahl_Eingabefeld, Hinzufuegen_Button, Auswahl_Button

    Zufallsauswahl_Liste = []

    def Eintrag_hinzufuegen():
        Eintrag = Zufallsauswahl_Eingabefeld.get()
        if Eintrag:
            Zufallsauswahl_Liste.append(Eintrag)
            Zufallsauswahl_Eingabefeld.delete(0, END)

    def zufall_auswaehlen():
        if Zufallsauswahl_Liste:
            zufaellige_Auswahl_aus_Liste = random.choice(Zufallsauswahl_Liste)
            Ergebnis_label = Label(fenster, text=zufaellige_Auswahl_aus_Liste, font=("Arial", 16))
            Ergebnis_label.grid(row=0, column=0)

    # Erst jetzt die Widgets erstellen und sichtbar machen
    Zufallsauswahl_Eingabefeld = Entry(fenster)
    Zufallsauswahl_Eingabefeld.grid(row=1, column=0)

    Hinzufuegen_Button = Button(fenster, text="Hinzufügen", command=Eintrag_hinzufuegen)
    Hinzufuegen_Button.grid(row=1, column=1)

    Auswahl_Button = Button(fenster, text="Ergebnis anzeigen", command=zufall_auswaehlen)
    Auswahl_Button.grid(row=2, column=0, columnspan=2)

def WoW_Auswahl():
    for widget in fenster.winfo_children ():
        widget.destroy ()
    WoW_Auswahlliste = ["Krieger", "Magier", "Paladin", "Jäger", "Schurke", "Priester", 
                         "Schamane", "Hexenmeister", "Mönch", "Druide", "Dämonenjäger", 
                         "Todesritter", "Rufer"]
    zufaellige_Auswahl_WoW = random.choice(WoW_Auswahlliste)
    WoW_label = Label(fenster, text=zufaellige_Auswahl_WoW, font=("Arial", 16))
    WoW_label.grid(row=0, column=0)

fenster = Tk()
fenster.title("Hauptmenü")
fenster.geometry ("800x500")

WoW_Button = Button(fenster, text="WoW", command=WoW_Auswahl)
WoW_Button.grid(row=0, column=0)

Zufallsauswahl_Button = Button(fenster, text="Zufallsauswahl aus erstellter Liste", command=Zufallsauswahl)
Zufallsauswahl_Button.grid(row=0, column=1)

fenster.mainloop()