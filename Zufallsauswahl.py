from tkinter import *
from Spieleauswahl import *

# Fenster erstellen
fenster = Tk()
fenster.title("Hauptmenü")
fenster.geometry("800x500")

# Funktion zum Entfernen aller Labels
def entfernen_aller_Labels():
    for widget in fenster.winfo_children():
        if isinstance(widget, Label) and widget != dropdown:  # Prüft, ob das Widget ein Label ist
            widget.destroy()

# Mapping von Spielen zu Funktionen
spiele_mapping = {
    "WoW": WoW_Auswahl,
    "Zufallsauswahl aus erstellter Liste": Zufallsauswahl,
    "Baldurs Gate 3": Baldurs_Gate_3_Auswahl,
    "Diablo 4": Diablo_4_Auswahl,
    "Monster Hunter Wilds/Rise/World": Monster_Hunter_Wilds_Rise_World_Auswahl,
    "Wild Hearts": Wild_Hearts_Auswahl,
    "Remnant 2": Remnant_2_Auswahl,
    "Last Epoch": Last_Epoch_Auswahl,
    "Lords of the Fallen": Lords_of_the_Fallen_Auswahl,
    "Oblivion": Oblivion_Auswahl,
    "Elden Ring": Elden_Ring_Auswahl,
    "For the King": For_the_King_Auswahl,
    "For the King 2": For_the_King_2_Auswahl,
    "Deep Rock Galactic": Deep_Rock_Galactic_Auswahl,
    "Terraria": Terraria_Auswahl,
    "Dragon's Dogma 2": Dragons_Dogma_2_Auswahl,
    "Divinity Original Sin 2": Divinity_Original_Sin_2_Auswahl,
}

# Liste der Spiele automatisch aus den Keys des Dictionaries erstellen
spiele = list(spiele_mapping.keys())

# Auswahlvariable für das Dropdown-Menü
auswahl = StringVar()
auswahl.set(spiele[0])  # Standardauswahl

# Funktion zur Auswahl eines Spiels
def spiel_auswahl(event):
    entfernen_aller_Labels()  # Zuerst alle Labels entfernen
    if auswahl.get() in spiele_mapping:
        spiele_mapping[auswahl.get()](fenster)

# Dropdown-Menü erstellen
dropdown = OptionMenu(fenster, auswahl, *spiele, command=spiel_auswahl)
dropdown.grid(row=0, column=0)

# Hauptloop starten
fenster.mainloop()