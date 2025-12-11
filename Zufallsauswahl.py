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
    "Baldurs Gate 3": lambda fenster: Spieleauswahl (fenster, Baldurs_Gate_3_Auswahlliste),
    "Barony": lambda fenster: Spieleauswahl (fenster, Barony_Auswahlliste),
    "Borderlands 2": lambda fenster: Spieleauswahl (fenster, Broderlands_2_Auswahlliste),
    "Borderlands 3": lambda fenster: Spieleauswahl (fenster, Borderlands_3_Auswahlliste),
    "Borderlands 4": lambda fenster: Spieleauswahl (fenster, Borderlands_4_Auswahlliste),
    "Dark Souls": lambda fenster: Spieleauswahl (fenster, Dark_Souls_Auswahlliste),
    "Dark Souls 2": lambda fenster: Spieleauswahl (fenster, Dark_Souls_2_Auswahlliste),
    "Dark Souls 3": lambda fenster: Spieleauswahl (fenster, Dark_Souls_3_Auswahlliste),
    "Deep Rock Galactic": lambda fenster: Spieleauswahl (fenster, Deep_Rock_Galactic_Auswahlliste),
    "Destiny 2" :lambda fenster: Spieleauswahl (fenster, Destiny_2_Auswahlliste),
    "Diablo 4": lambda fenster: Spieleauswahl (fenster, Diablo_4_Auswahlliste),
    "Divinity Original Sin 2": lambda fenster: Spieleauswahl (fenster, Divinity_Original_Sin_2_Auswahlliste),
    "Dota 2": lambda fenster: Spieleauswahl (fenster, Dota_2_Auswahlliste),
    "Dragon's Dogma" : lambda fenster: Spieleauswahl (fenster, Dragons_Dogma_Auswahlliste),
    "Dragon's Dogma 2": lambda fenster: Spieleauswahl (fenster, Dragons_Dogma_2_Auswahlliste),
    "Elden Ring": lambda fenster: Spieleauswahl (fenster, Elden_Ring_Auswahlliste),
    "Fallout 76": lambda fenster: Spieleauswahl (fenster, Fallout_76_Auswahlliste),
    "Final Fantasy XIV (Online)": lambda fenster: Spieleauswahl (fenster, Final_Fantasy_XIV_Auswahlliste),
    "For the King": lambda fenster: Spieleauswahl (fenster, For_the_King_Auswahlliste),
    "For the King 2": lambda fenster: Spieleauswahl (fenster, For_the_King_2_Auswahlliste),
    "Guild Wars 2": lambda fenster: Spieleauswahl (fenster, Guild_Wars_2_Auswahlliste),
    "Last Epoch": lambda fenster: Spieleauswahl (fenster, Last_Epoch_Auswahlliste),
    "Lords of the Fallen": lambda fenster: Spieleauswahl (fenster, Lords_of_the_Fallen_Auswahlliste),
    "Monster Hunter Wilds/Rise/World": lambda fenster: Spieleauswahl (fenster, Monster_Hunter_Wilds_Rise_World_Auswahlliste),
    "Monster Hunter Stories 2": lambda fenster: Spieleauswahl (fenster, Monster_Hunter_Stories_2_Auswahlliste),
    "Oblivion": lambda fenster: Spieleauswahl (fenster, Oblivion_Auswahlliste),
    "Pathfinder: Wrath of the Righteous": lambda fenster: Spieleauswahl (fenster, Pathfinder_Wrath_of_the_Righteous_Auswahlliste),
    "Remnant 2": lambda fenster: Spieleauswahl (fenster, Remnant_2_Auswahlliste),
    "Shakes and Fidget": lambda fenster: Spieleauswahl (fenster, Shakes_and_Fidget_Auswahlliste),
    "SWTOR": lambda fenster: Spieleauswahl (fenster, SWTOR_Auswahlliste),
    "Tainted Grail: Fall of Avalon": lambda fenster: Spieleauswahl (fenster, Tainted_Grail_Fall_of_Avalon_Auswahlliste),
    "Terraria": lambda fenster: Spieleauswahl (fenster, Terraria_Auswahlliste),
    "The Elder Scrolls Online": lambda fenster: Spieleauswahl (fenster, The_Elder_Scrolls_Online_Auswahlliste),
    "The Outer Worlds": lambda fenster: Spieleauswahl (fenster, The_Outer_Worlds_Auswahlliste),
    "The Outer Worlds 2": lambda fenster: Spieleauswahl (fenster, The_Outer_Worlds_2_Auswahlliste),
    "Warhammer Vermintdie 2": lambda fenster: Spieleauswahl (fenster, Warhammer_Vermintide_2_Auswahlliste),
    "Wild Hearts": lambda fenster: Spieleauswahl (fenster, Wild_Hearts_Auswahlliste),
    "WoW": lambda fenster: Spieleauswahl (fenster, WoW_Auswahlliste),
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
