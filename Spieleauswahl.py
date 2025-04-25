import random
from tkinter import *

def erneut_Ausfuehren (fenster, Auswahl):
    erneut_Ausfuehren_button = Button (fenster, text="Erneut ausführen", command=lambda:Auswahl (fenster))
    erneut_Ausfuehren_button.grid (row=1, column=0)
    
def Zufallsauswahl(fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()

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

    Zufallsauswahl_Eingabefeld = Entry(fenster)
    Zufallsauswahl_Eingabefeld.grid(row=1, column=0)

    Hinzufuegen_Button = Button(fenster, text="Hinzufügen", command=Eintrag_hinzufuegen)
    Hinzufuegen_Button.grid(row=1, column=1)

    Auswahl_Button = Button(fenster, text="Ergebnis anzeigen", command=zufall_auswaehlen)
    Auswahl_Button.grid(row=2, column=0, columnspan=2)

    erneut_Ausfuehren (fenster, Zufallsauswahl)

def WoW_Auswahl(fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    WoW_Auswahlliste = ["Krieger", "Magier", "Paladin", "Jäger", "Schurke", "Priester", 
                         "Schamane", "Hexenmeister", "Mönch", "Druide", "Dämonenjäger", 
                         "Todesritter", "Rufer"]
    zufaellige_Auswahl_WoW = random.choice(WoW_Auswahlliste)
    WoW_label = Label(fenster, text=zufaellige_Auswahl_WoW, font=("Arial", 16))
    WoW_label.grid(row=0, column=0)

    erneut_Ausfuehren (fenster, WoW_Auswahl)

def Baldurs_Gate_3_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Baldurs_Gate_3_Auswahlliste = ["Barbar", "Barde", "Druide", "Hexenmeister", 
                                   "Kämpfer", "Kleriker", "Magier", "Mönch", "Paladin", 
                                   "Schurke", "Waldläufer", "Zauberer"]
    zufaellige_Auswahl_Baldurs_Gate_3 = random.choice (Baldurs_Gate_3_Auswahlliste)
    Baldurs_Gate_3_label = Label (fenster, text=zufaellige_Auswahl_Baldurs_Gate_3, font = ("Arial", 16))
    Baldurs_Gate_3_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Baldurs_Gate_3_Auswahl)

def Diablo_4_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Diablo_4_Auswahlliste = ["Barbar", "Druide", "Geistgeborener", "Jäger", "Totenbeschwörer", "Zauberer"]
    zufaellige_Auswahl_Diablo_4 = random.choice (Diablo_4_Auswahlliste)
    Diablo_4_label = Label (fenster, text=zufaellige_Auswahl_Diablo_4, font=("Arial", 16))
    Diablo_4_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Diablo_4_Auswahl)

def Monster_Hunter_Wilds_Rise_World_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Monster_Hunter_Wilds_Rise_World_Auswahlliste = ["Langschwert", "Bogen", "Doppelklingen", "Gewehrlanze", "Großschwert", "schweres Bogengewehr",
                                                    "Energieklinge", "Jagdhorn", "Schwert und Schild", "Morph-Axt", "leichtes Bogengewehr",
                                                    "Hammer", "Insektengleve", "Lanze"]
    zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World = random.choice (Monster_Hunter_Wilds_Rise_World_Auswahlliste)
    Monster_Hunter_Wilds_Rise_World_label = Label (fenster, text=zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World, font=("Arial", 16))
    Monster_Hunter_Wilds_Rise_World_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Monster_Hunter_Wilds_Rise_World_Auswahl)

def Wild_Hearts_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Wild_Hearts_Auswahlliste = ["Krallenklinge", "Bogen", "Karakuri-Katana", "Nodachi", "Handkanone", "Karakuri-Stab", "Hammer", "Klingen-Wagasa"]
    zufaellige_Auswahl_Wild_Hearts = random.choice (Wild_Hearts_Auswahlliste)
    Wild_Hearts_label = Label (fenster, text=zufaellige_Auswahl_Wild_Hearts, font=("Arial", 16))
    Wild_Hearts_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Wild_Hearts_Auswahl)

def Remnant_2_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Remnant_2_Auswahlliste = ["Alchemist", "Archon", "Challenger", "Engineer", "Explorer", "Gunslinger", "Handler", "Hunter", "Invader",
                             "Invoker", "Medic", "Summoner", "Ritualist", "Warden"]
    zufaellige_Auswahl_Remnant_2 = random.choice (Remnant_2_Auswahlliste)
    Remnant_2_label = Label (fenster, text=zufaellige_Auswahl_Remnant_2, font=("Arial", 16))
    Remnant_2_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Remnant_2_Auswahl)

def Last_Epoch_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Last_Epoch_Auswahlliste = ["Mage", "Primalist", "Acolyte", "Rogue", "Sentinel"]
    zufaellige_Auswahl_Last_Epoch = random.choice (Last_Epoch_Auswahlliste)
    Last_Epoch_label = Label (fenster, text=zufaellige_Auswahl_Last_Epoch, font=("Arial", 16))
    Last_Epoch_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Last_Epoch_Auswahl)

def Lords_of_the_Fallen_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Lords_of_the_Fallen_Auswahlliste = ["Heliger Ritter", "Udirangr-Kriegswolf", "Partisan", "Mournstead-Infanterie", "Schwarzfeder-Waldläufer",
                                       "Verbannter Nachsteller", "Prediger Orius", "Feuerkultist", "Verdammter"]
    zufaellige_Auswahl_Lords_of_the_Fallen = random.choice (Lords_of_the_Fallen_Auswahlliste)
    Lords_of_the_Fallen_label = Label (fenster, text=zufaellige_Auswahl_Lords_of_the_Fallen, font=("Arial", 16))
    Lords_of_the_Fallen_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Lords_of_the_Fallen_Auswahl)

def Oblivion_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Oblivion_Auswahlliste = ["Agent", "Akrobat", "Assassine", "Barbar", "Barde", "Bogenschütze", "Dieb", "Heiler", "Hexenjäger", "Hexer", "Kampfmagier",
                             "Kreuzritter", "Krieger", "Kundschafter", "Magier", "Mönch", "Pilger", "Ritter", "Schattenklinge", "Schurke", "Schwertmagier"]
    zufaellige_Auswahl_Oblivion = random.choice (Oblivion_Auswahlliste)
    Oblivion_label = Label (fenster, text=zufaellige_Auswahl_Oblivion, font=("Arial", 16))
    Oblivion_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Oblivion_Auswahl)

def Elden_Ring_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Elden_Ring_Auswahlliste = ["Held", "Bandit", "Astrologe", "Krieger", "Gefangener", "Bekenner", "Bettler", "Vagabund", "Prophet", "Samurai"]
    zufaellige_Auswahl_Elden_Ring = random.choice (Elden_Ring_Auswahlliste)
    Elden_Ring_label = Label (fenster, text=zufaellige_Auswahl_Elden_Ring, font=("Arial", 16))
    Elden_Ring_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Elden_Ring_Auswahl)

def For_the_King_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    For_the_King_Auswahlliste = ["Schmied", "Jäger", "Minnesänger", "Gelehrter", "Straßenmusiker", "Kräuterkundlerin", "Fallensteller",
                                 "Holzfäller", "Hobo", "Mönch", "Schatzsucher", "Astronom", "Gladiator"]
    zufaellige_Auswahl_For_the_King = random.choice (For_the_King_Auswahlliste)
    For_the_King_label = Label (fenster, text=zufaellige_Auswahl_For_the_King, font=("Arial", 16))
    For_the_King_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, For_the_King_Auswahl)

def For_the_King_2_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    For_the_King_2_Auswahlliste = ["Alchemist", "Schmied", "Straßenmusiker", "Bauer", "Mönch", "Kräuterkundlerin", "Hobo", "Jäger",
                                   "Minnesänger", "Pfadfinder", "Gelehrter", "Hirte", "Stallbursche", "Holzfäller"]
    zufaellige_Auswahl_For_the_King_2 = random.choice (For_the_King_2_Auswahlliste)
    For_the_King_2_label = Label (fenster, text=zufaellige_Auswahl_For_the_King_2, font=("Arial", 16))
    For_the_King_2_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, For_the_King_2_Auswahl)

def Deep_Rock_Galactic_Auswahl (fenster):
    for widget in fenster.winfo_children ():
        widget.destroy ()
    Deep_Rock_Galactic_Auswahlliste = ["Ingenieur", "Schütze", "Bohrer", "Späher"]
    zufaellige_Auswahl_Deep_Rock_Galactic = random.choice (Deep_Rock_Galactic_Auswahlliste)
    Deep_Rock_Galactic_label = Label (fenster, text=zufaellige_Auswahl_Deep_Rock_Galactic, font=("Arial", 16))
    Deep_Rock_Galactic_label.grid (row=0, column=0)

    erneut_Ausfuehren (fenster, Deep_Rock_Galactic_Auswahl)
