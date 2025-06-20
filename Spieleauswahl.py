import random
from tkinter import *

def erneut_Ausfuehren (fenster, Auswahl, label_to_destroy):
    def destroy_label ():
        label_to_destroy.destroy ()
    
    def combined_function ():
        destroy_label ()
        Auswahl (fenster)

    erneut_Ausfuehren_button = Button (fenster, text="Erneut ausführen", command=combined_function)
    erneut_Ausfuehren_button.grid (row=4, column=0)
    
def Zufallsauswahl(fenster):
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
            Ergebnis_label.grid(row=1, column=0)

    Zufallsauswahl_Eingabefeld = Entry(fenster)
    Zufallsauswahl_Eingabefeld.grid(row=2, column=0)

    Hinzufuegen_Button = Button(fenster, text="Hinzufügen", command=Eintrag_hinzufuegen)
    Hinzufuegen_Button.grid(row=3, column=0)

    Auswahl_Button = Button(fenster, text="Ergebnis anzeigen", command=zufall_auswaehlen)
    Auswahl_Button.grid(row=3, column=1, columnspan=2)


def WoW_Auswahl(fenster):
    WoW_Auswahlliste = ["Krieger", "Magier", "Paladin", "Jäger", "Schurke", "Priester", 
                         "Schamane", "Hexenmeister", "Mönch", "Druide", "Dämonenjäger", 
                         "Todesritter", "Rufer"]
    zufaellige_Auswahl_WoW = random.choice(WoW_Auswahlliste)
    WoW_label = Label(fenster, text=zufaellige_Auswahl_WoW, font=("Arial", 16))
    WoW_label.grid(row=1, column=0)

    erneut_Ausfuehren (fenster, WoW_Auswahl, WoW_label)

def Baldurs_Gate_3_Auswahl (fenster):
    Baldurs_Gate_3_Auswahlliste = ["Barbar", "Barde", "Druide", "Hexenmeister", 
                                   "Kämpfer", "Kleriker", "Magier", "Mönch", "Paladin", 
                                   "Schurke", "Waldläufer", "Zauberer"]
    zufaellige_Auswahl_Baldurs_Gate_3 = random.choice (Baldurs_Gate_3_Auswahlliste)
    Baldurs_Gate_3_label = Label (fenster, text=zufaellige_Auswahl_Baldurs_Gate_3, font = ("Arial", 16))
    Baldurs_Gate_3_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Baldurs_Gate_3_Auswahl, Baldurs_Gate_3_label)

def Diablo_4_Auswahl (fenster):
    Diablo_4_Auswahlliste = ["Barbar", "Druide", "Geistgeborener", "Jäger", "Totenbeschwörer", "Zauberer"]
    zufaellige_Auswahl_Diablo_4 = random.choice (Diablo_4_Auswahlliste)
    Diablo_4_label = Label (fenster, text=zufaellige_Auswahl_Diablo_4, font=("Arial", 16))
    Diablo_4_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Diablo_4_Auswahl, Diablo_4_label)

def Monster_Hunter_Wilds_Rise_World_Auswahl (fenster):
    Monster_Hunter_Wilds_Rise_World_Auswahlliste = ["Langschwert", "Bogen", "Doppelklingen", "Gewehrlanze", "Großschwert", "schweres Bogengewehr",
                                                    "Energieklinge", "Jagdhorn", "Schwert und Schild", "Morph-Axt", "leichtes Bogengewehr",
                                                    "Hammer", "Insektengleve", "Lanze"]
    zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World = random.choice (Monster_Hunter_Wilds_Rise_World_Auswahlliste)
    Monster_Hunter_Wilds_Rise_World_label = Label (fenster, text=zufaellige_Auswahl_Monster_Hunter_Wilds_Rise_World, font=("Arial", 16))
    Monster_Hunter_Wilds_Rise_World_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Monster_Hunter_Wilds_Rise_World_Auswahl, Monster_Hunter_Wilds_Rise_World_label)

def Wild_Hearts_Auswahl (fenster):
    Wild_Hearts_Auswahlliste = ["Krallenklinge", "Bogen", "Karakuri-Katana", "Nodachi", "Handkanone", "Karakuri-Stab", "Hammer", "Klingen-Wagasa"]
    zufaellige_Auswahl_Wild_Hearts = random.choice (Wild_Hearts_Auswahlliste)
    Wild_Hearts_label = Label (fenster, text=zufaellige_Auswahl_Wild_Hearts, font=("Arial", 16))
    Wild_Hearts_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Wild_Hearts_Auswahl, Wild_Hearts_label)

def Remnant_2_Auswahl (fenster):
    Remnant_2_Auswahlliste = ["Alchemist", "Archon", "Challenger", "Engineer", "Explorer", "Gunslinger", "Handler", "Hunter", "Invader",
                             "Invoker", "Medic", "Summoner", "Ritualist", "Warden"]
    zufaellige_Auswahl_Remnant_2 = random.choice (Remnant_2_Auswahlliste)
    Remnant_2_label = Label (fenster, text=zufaellige_Auswahl_Remnant_2, font=("Arial", 16))
    Remnant_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Remnant_2_Auswahl, Remnant_2_label)

def Last_Epoch_Auswahl (fenster):
    Last_Epoch_Auswahlliste = ["Mage", "Primalist", "Acolyte", "Rogue", "Sentinel"]
    zufaellige_Auswahl_Last_Epoch = random.choice (Last_Epoch_Auswahlliste)
    Last_Epoch_label = Label (fenster, text=zufaellige_Auswahl_Last_Epoch, font=("Arial", 16))
    Last_Epoch_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Last_Epoch_Auswahl, Last_Epoch_label)

def Lords_of_the_Fallen_Auswahl (fenster):
    Lords_of_the_Fallen_Auswahlliste = ["Heliger Ritter", "Udirangr-Kriegswolf", "Partisan", "Mournstead-Infanterie", "Schwarzfeder-Waldläufer",
                                       "Verbannter Nachsteller", "Prediger Orius", "Feuerkultist", "Verdammter"]
    zufaellige_Auswahl_Lords_of_the_Fallen = random.choice (Lords_of_the_Fallen_Auswahlliste)
    Lords_of_the_Fallen_label = Label (fenster, text=zufaellige_Auswahl_Lords_of_the_Fallen, font=("Arial", 16))
    Lords_of_the_Fallen_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Lords_of_the_Fallen_Auswahl, Lords_of_the_Fallen_label)

def Oblivion_Auswahl (fenster):
    Oblivion_Auswahlliste = ["Agent", "Akrobat", "Assassine", "Barbar", "Barde", "Bogenschütze", "Dieb", "Heiler", "Hexenjäger", "Hexer", "Kampfmagier",
                             "Kreuzritter", "Krieger", "Kundschafter", "Magier", "Mönch", "Pilger", "Ritter", "Schattenklinge", "Schurke", "Schwertmagier"]
    zufaellige_Auswahl_Oblivion = random.choice (Oblivion_Auswahlliste)
    Oblivion_label = Label (fenster, text=zufaellige_Auswahl_Oblivion, font=("Arial", 16))
    Oblivion_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Oblivion_Auswahl, Oblivion_label)

def Elden_Ring_Auswahl (fenster):
    Elden_Ring_Auswahlliste = ["Held", "Bandit", "Astrologe", "Krieger", "Gefangener", "Bekenner", "Bettler", "Vagabund", "Prophet", "Samurai"]
    zufaellige_Auswahl_Elden_Ring = random.choice (Elden_Ring_Auswahlliste)
    Elden_Ring_label = Label (fenster, text=zufaellige_Auswahl_Elden_Ring, font=("Arial", 16))
    Elden_Ring_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Elden_Ring_Auswahl, Elden_Ring_label)

def For_the_King_Auswahl (fenster):
    For_the_King_Auswahlliste = ["Schmied", "Jäger", "Minnesänger", "Gelehrter", "Straßenmusiker", "Kräuterkundlerin", "Fallensteller",
                                 "Holzfäller", "Hobo", "Mönch", "Schatzsucher", "Astronom", "Gladiator"]
    zufaellige_Auswahl_For_the_King = random.choice (For_the_King_Auswahlliste)
    For_the_King_label = Label (fenster, text=zufaellige_Auswahl_For_the_King, font=("Arial", 16))
    For_the_King_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, For_the_King_Auswahl, For_the_King_label)

def For_the_King_2_Auswahl (fenster):
    For_the_King_2_Auswahlliste = ["Alchemist", "Schmied", "Straßenmusiker", "Bauer", "Mönch", "Kräuterkundlerin", "Hobo", "Jäger",
                                   "Minnesänger", "Pfadfinder", "Gelehrter", "Hirte", "Stallbursche", "Holzfäller"]
    zufaellige_Auswahl_For_the_King_2 = random.choice (For_the_King_2_Auswahlliste)
    For_the_King_2_label = Label (fenster, text=zufaellige_Auswahl_For_the_King_2, font=("Arial", 16))
    For_the_King_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, For_the_King_2_Auswahl, For_the_King_2_label)

def Deep_Rock_Galactic_Auswahl (fenster):
    Deep_Rock_Galactic_Auswahlliste = ["Ingenieur", "Schütze", "Bohrer", "Späher"]
    zufaellige_Auswahl_Deep_Rock_Galactic = random.choice (Deep_Rock_Galactic_Auswahlliste)
    Deep_Rock_Galactic_label = Label (fenster, text=zufaellige_Auswahl_Deep_Rock_Galactic, font=("Arial", 16))
    Deep_Rock_Galactic_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Deep_Rock_Galactic_Auswahl, Deep_Rock_Galactic_label)

def Terraria_Auswahl (fenster):
    Terraria_Auswahlliste = ["Nahkämpfer", "Magier", "Fernkämpfer", "Beschwörer"]
    zufaellige_Auswahl_Terraria = random.choice (Terraria_Auswahlliste)
    Terraria_label = Label (fenster, text=zufaellige_Auswahl_Terraria, font=("Arial", 16))
    Terraria_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Terraria_Auswahl, Terraria_label)

def Dragons_Dogma_2_Auswahl (fenster):
    Dragons_Dogma_2_Auswahlliste = ["Kämpfer", "Bogenschütze", "Magier", "Dieb", "Krieger", "Magiebogenschütze", "mystische Klinge",
                                    "Erzmagier", "Illusionist", "Kriegsmeister"]
    zufaellige_Auswahl_Dragons_Dogma_2 = random.choice (Dragons_Dogma_2_Auswahlliste)
    Dragons_Dogma_2_label = Label (fenster, text=zufaellige_Auswahl_Dragons_Dogma_2, font=("Arial", 16))
    Dragons_Dogma_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Dragons_Dogma_2_Auswahl, Dragons_Dogma_2_label)

def Divinity_Original_Sin_2_Auswahl (fenster):
    Divinity_Original_Sin_2_Auswahlliste = ["Hexe", "Zauberer", "Kampfmagier", "Beschwörer", "Verzauberer", "Kämpfer", "Inquisitor", "Metamorph",
                                       "Ritter", "Kleriker", "Schattenklinge", "Schurke", "Waldläufer", "Wildling"]
    zufaellige_Auswahl_Divinity_Original_Sin_2 = random.choice (Divinity_Original_Sin_2_Auswahlliste)
    Divinity_Original_Sin_2_label = Label (fenster, text=zufaellige_Auswahl_Divinity_Original_Sin_2, font=("Arial", 16))
    Divinity_Original_Sin_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Divinity_Original_Sin_2_Auswahl, Divinity_Original_Sin_2_label)

def Shakes_and_Fidget_Auswahl (fenster):
    Shakes_and_Fidget_Auswahlliste = ["Paladin", "Druide", "Berserker", "Magier", "Kundschafter", "Kampfmagier", "Assassine", "Krieger",
                                      "Dämonenjäger", "Barde", "Nekromant"]
    zufaellige_Auswahl_Shakes_and_Fidget = random.choice (Shakes_and_Fidget_Auswahlliste)
    Shakes_and_Fidget_label = Label (fenster, text=zufaellige_Auswahl_Shakes_and_Fidget, font=("Arial", 16))
    Shakes_and_Fidget_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Shakes_and_Fidget_Auswahl, Shakes_and_Fidget_label)
    
def Borderlands_4_Auswahl (fenster):
    Borderlands_4_Auswahlliste = ["Amon", "Harlowe", "Rafa", "Vex"]
    zufaellige_Auswahl_Borderlands_4 = random.choice (Borderlands_4_Auswahlliste)
    Borderlands_4_label = Label (fenster, text=zufaellige_Auswahl_Borderlands_4, font=("Arial", 16))
    Borderlands_4_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Borderlands_4_Auswahl, Borderlands_4_label)

def Fallout_76_Auswahl (fenster):
    Fallout_76_Auswahlliste = ["Pistolen", "nicht-automatisches Gewehr", "vollautomatisches Gewehr", "Bogen / Armbrust", "Shotguns", "schwere Waffen", "explosive Gewehre",
                               "einhand Nahkampf", "zweihand Nahkampf", "Faustwaffen"]
    zufaellige_Auswahl_Fallout_76 = random.choice (Fallout_76_Auswahlliste)
    Fallout_76_label = Label (fenster, text=zufaellige_Auswahl_Fallout_76, font=("Arial", 16))
    Fallout_76_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Fallout_76_Auswahl, Fallout_76_label)

def Warhammer_Vermintide_2_Auswahl (fenster):
    Warhammer_Vermintide_2_Auswahlliste = ["Bardin Goreksson", "Kerillian", "Victor Saltzbrand", "Markus Kruber", "Sienna Fuegonasus"]
    zufaellige_Auswahl_Warhammer_Vermintide_2 = random.choice (Warhammer_Vermintide_2_Auswahlliste)
    Warhammer_Vermintide_2_label = Label (fenster, text=zufaellige_Auswahl_Warhammer_Vermintide_2, font=("Arial", 16))
    Warhammer_Vermintide_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Warhammer_Vermintide_2_Auswahl, Warhammer_Vermintide_2_label)

def Dark_Souls_Auswahl (fenster):
    Dark_Souls_Auswahlliste = ["Krieger", "Ritter", "Vagabund", "Dieb", "Bandit", "Jäger", "Zauberer", "Pyromant", "Kleriker", "Bettler"]
    zufaellige_Auswahl_Dark_Souls = random.choice (Dark_Souls_Auswahlliste)
    Dark_Souls_label = Label (fenster, text=zufaellige_Auswahl_Dark_Souls, font=("Arial", 16))
    Dark_Souls_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Dark_Souls_Auswahl, Dark_Souls_label)

def Dark_Souls_2_Auswahl (fenster):
    Dark_Souls_2_Auswahlliste = ["Krieger", "Ritter", "Schwertkämpfer", "Bandit", "Kleriker", "Zauberer", "Erkunder", "Bettler",]
    zufaellige_Auswahl_Dark_Souls_2 = random.choice (Dark_Souls_2_Auswahlliste)
    Dark_Souls_2_label = Label (fenster, text=zufaellige_Auswahl_Dark_Souls_2, font=("Arial", 16))
    Dark_Souls_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Dark_Souls_2_Auswahl, Dark_Souls_2_label)

def Dark_Souls_3_Auswahl (fenster):
    Dark_Souls_3_Auswahlliste = ["Ritter", "Söldner", "Krieger", "Herold", "Dieb", "Assassine", "Zauberer", "Pyromant", "Kleriker", "Bettler"]
    zufaellige_Auswahl_Dark_Souls_3 = random.choice (Dark_Souls_3_Auswahlliste)
    Dark_Souls_3_label = Label (fenster, text=zufaellige_Auswahl_Dark_Souls_3, font=("Arial", 16))
    Dark_Souls_3_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Dark_Souls_3_Auswahl, Dark_Souls_3_label)

def Destiny_2_Auswahl (fenster):
    Destiny_2_Auswahlliste = ["Warlock", "Jäger", "Titan"]
    zufaellige_Auswahl_Destiny_2 = random.choice (Destiny_2_Auswahlliste)
    Destiny_2_label = Label (fenster, text=zufaellige_Auswahl_Destiny_2, font=("Arial", 16))
    Destiny_2_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Destiny_2_Auswahl, Destiny_2_label)

def The_Elder_Scrolls_Online_Auswahl (fenster):
    The_Elder_Scrolls_Online_Auswahlliste = ["Drachenritter", "Zauberer", "Nachtklinge", "Hüter", "Nekromant", "Templer", "Arkanist"]
    zufaellige_Auswahl_The_Elder_Scrolls_Online = random.choice (The_Elder_Scrolls_Online_Auswahlliste)
    The_Elder_Scrolls_Online_label = Label (fenster, text=zufaellige_Auswahl_The_Elder_Scrolls_Online, font=("Arial", 16))
    The_Elder_Scrolls_Online_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, The_Elder_Scrolls_Online_Auswahl, The_Elder_Scrolls_Online_label)

def SWTOR_Auswahl (fenster):
    SWTOR_Auswahlliste = ["Jedi-Botschafter", "Imperialer Agent", "Jedi-Ritter", "Kopfgeldjäger", "Schmuggler", "Sith-Inquisitor", "Soldat", "Sith-Krieger"]
    zufaellige_Auswahl_SWTOR = random.choice (SWTOR_Auswahlliste)
    SWTOR_label = Label (fenster, text=zufaellige_Auswahl_SWTOR, font=("Arial", 16))
    SWTOR_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, SWTOR_Auswahl, SWTOR_label)

def Final_Fantasy_XIV_Auswahl (fenster):
    Final_Fantasy_XIV_Auswahlliste = ["Paladin", "Krieger", "Dunkelritter", "Revolverklinge", "Weißmagier", "Gelehrter", "Astrologe", "Weiser", "Mönch",
                                      "Dragoon", "Ninja", "Samurai", "Schnitter", "Viper", "Barde", "Maschinist", "Tänzer", "Schwarzmagier",
                                      "Beschwörer", "Rotmagier", "Piktomant", "Blaumagier"]
    zufaellige_Auswahl_Final_Fantasy_XIV = random.choice (Final_Fantasy_XIV_Auswahlliste)
    Final_Fantasy_XIV_label = Label (fenster, text=zufaellige_Auswahl_Final_Fantasy_XIV, font=("Arial", 16))
    Final_Fantasy_XIV_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Final_Fantasy_XIV_Auswahl, Final_Fantasy_XIV_label)

def Dragons_Dogma_Auswahl (fenster):
    Dragons_Dogma_Auswahlliste = ["Kämpfer", "Magier", "Streicher", "Krieger", "Erzmagier", "Waldläufer", "Assassine", "Mystischer Ritter", "Magischer Bogenschütze"]
    zufaellige_Auswahl_Dragons_Dogma = random.choice (Dragons_Dogma_Auswahlliste)
    Dragons_Dogma_label = Label (fenster, text=zufaellige_Auswahl_Dragons_Dogma, font=("Arial", 16))
    Dragons_Dogma_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Dragons_Dogma_Auswahl, Dragons_Dogma_label)

def Barony_Auswahl (fenster):
    Barony_Auswahlliste = ["Barbarian", "Warrior", "Healer", "Rogue", "Wizard", "Merchant", "Cleric", "Wanderer", "Arcanist", "Joker", "Sexton", "Ninja", "Mesmer", "Accursed",
                          "Conjurer", "Monk", "Brewer", "Mechanist", "Punisher", "Shaman", "Hunter"]
    zufaellige_Auswahl_Barony = random.choice (Barony_Auswahlliste)
    Barony_label = Label (fenster, text=zufaellige_Auswahl_Barony, font=("Arial", 16))
    Barony_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, Barony_Auswahl, Barony_label)
