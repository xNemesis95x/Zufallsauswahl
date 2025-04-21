import random
from tkinter import *

def Zufallsauswahl(fenster):
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

def WoW_Auswahl(fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    WoW_Auswahlliste = ["Krieger", "Magier", "Paladin", "Jäger", "Schurke", "Priester", 
                         "Schamane", "Hexenmeister", "Mönch", "Druide", "Dämonenjäger", 
                         "Todesritter", "Rufer"]
    zufaellige_Auswahl_WoW = random.choice(WoW_Auswahlliste)
    WoW_label = Label(fenster, text=zufaellige_Auswahl_WoW, font=("Arial", 16))
    WoW_label.grid(row=0, column=0)

def Baldurs_Gate_3_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Baldurs_Gate_3_Auswahlliste = ["Barbar", "Barde", "Druide", "Hexenmeister", 
                                   "Kämpfer", "Kleriker", "Magier", "Mönch", "Paladin", 
                                   "Schurke", "Waldläufer", "Zauberer"]
    zufaellige_Auswahl_Baldurs_Gate_3 = random.choice (Baldurs_Gate_3_Auswahlliste)
    Baldurs_Gate_3_label = Label (fenster, text=zufaellige_Auswahl_Baldurs_Gate_3, font = ("Arial", 16))
    Baldurs_Gate_3_label.grid (row=0, column=0)

def Diablo_4_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Diablo_4_Auswahlliste = ["Barbar", "Druide", "Geistgeborener", "Jäger", "Totenbeschwörer", "Zauberer"]
    zufaellige_Auswahl_Diablo_4 = random.choice (Diablo_4_Auswahlliste)
    Diablo_4_label = Label (fenster, text=zufaellige_Auswahl_Diablo_4, font=("Arial", 16))
    Diablo_4_label.grid (row=0, column=0)

def Monster_Hunter_Wilds_Rise_World_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Monster_Hunter_Wilds_Rise_World_Auswahlliste = ["Langschwert", "Bogen", "Doppelklingen", "Gewehrlanze", "Großschwert", "schweres Bogengewehr",
                                                    "Energieklinge", "Jagdhorn", "Schwert und Schild", "Morph-Axt", "leichtes Bogengewehr",
                                                    "Hammer", "Insektengleve", "Lanze"]
    zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World = random.choice (Monster_Hunter_Wilds_Rise_World_Auswahlliste)
    Monster_Hunter_Wilds_Rise_World_label = Label (fenster, text=zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World, font=("Arial", 16))
    Monster_Hunter_Wilds_Rise_World_label.grid (row=0, column=0)