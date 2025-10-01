import random
from tkinter import *
from tkinter.ttk import Combobox
from Spieleauswahl import *

# Fenster erstellen
fenster = Tk()
fenster.title("Hauptmenü")
fenster.geometry("800x500")

# Funktion zum Entfernen aller Labels
def entfernen_aller_Labels():
    for widget in fenster.winfo_children():
        if isinstance(widget, Label):  # Nur Labels entfernen, damit Combobox erhalten bleibt
            widget.destroy()

# Mapping von Spielen zu Funktionen
spiele_mapping = {
    "Baldurs Gate 3": Baldurs_Gate_3_Auswahl,
    "Barony": Barony_Auswahl,
    "Borderlands 2": Broderlands_2_Auswahl,
    "Borderlands 3": Borderlands_3_Auswahl,
    "Borderlands 4": Borderlands_4_Auswahl,
    "Dark Souls": Dark_Souls_Auswahl,
    "Dark Souls 2": Dark_Souls_2_Auswahl,
    "Dark Souls 3": Dark_Souls_3_Auswahl,
    "Deep Rock Galactic": Deep_Rock_Galactic_Auswahl,
    "Destiny 2" : Destiny_2_Auswahl,
    "Diablo 4": Diablo_4_Auswahl,
    "Divinity Original Sin 2": Divinity_Original_Sin_2_Auswahl,
    "Dragon's Dogma" : Dragons_Dogma_Auswahl,
    "Dragon's Dogma 2": Dragons_Dogma_2_Auswahl,
    "Elden Ring": Elden_Ring_Auswahl,
    "Fallout 76": Fallout_76_Auswahl,
    "Final Fantasy XIV (Online)": Final_Fantasy_XIV_Auswahl,
    "For the King": For_the_King_Auswahl,
    "For the King 2": For_the_King_2_Auswahl,
    "Guild Wars 2": Guild_Wars_2_Auswahl,
    "Last Epoch": Last_Epoch_Auswahl,
    "Lords of the Fallen": Lords_of_the_Fallen_Auswahl,
    "Monster Hunter Wilds/Rise/World": Monster_Hunter_Wilds_Rise_World_Auswahl,
    "Monster Hunter Stories 2": Monster_Hunter_Stories_2_Auswahl,
    "Oblivion": Oblivion_Auswahl,
    "Pathfinder: Wrath of the Righteous" : Pathfinder_Wrath_of_the_Righteous_Auswahl,
    "Remnant 2": Remnant_2_Auswahl,
    "Shakes and Fidget": Shakes_and_Fidget_Auswahl,
    "SWTOR": SWTOR_Auswahl,
    "Terraria": Terraria_Auswahl,
    "The Elder Scrolls Online": The_Elder_Scrolls_Online_Auswahl,
    "Warhammer Vermintdie 2": Warhammer_Vermintide_2_Auswahl,
    "Wild Hearts": Wild_Hearts_Auswahl,
    "WoW": WoW_Auswahl,
    "Zufallsauswahl aus erstellter Liste": Zufallsauswahl
}

# Liste der Spiele automatisch aus den Keys des Dictionaries erstellen
spiele = list(spiele_mapping.keys())

# Auswahlvariable für die Combobox
auswahl = StringVar()
auswahl.set("Wähle ein Spiel")  # Standardauswahl

# Funktion zur Auswahl eines Spiels
def spiel_auswahl(event=None):  # event=None erlaubt das Aufrufen der Funktion ohne Event-Parameter
    entfernen_aller_Labels()  # Zuerst alle Labels entfernen
    if auswahl.get() in spiele_mapping:
        spiele_mapping[auswahl.get()](fenster)

# Combobox erstellen
combobox = Combobox(fenster, textvariable=auswahl, values=spiele, state="readonly")  # "readonly" verhindert manuelle Eingabe
combobox.grid(row=0, column=0)
combobox.bind("<<ComboboxSelected>>", spiel_auswahl)  # Ruft die Funktion auf, wenn eine Auswahl getroffen wird

# Hauptloop starten
fenster.mainloop()
