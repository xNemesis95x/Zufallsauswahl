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

def Spieleauswahl (fenster, liste):
    zufaellige_Auswahl_spiel = random.choice (liste)
    spielename_label = Label (fenster, text=zufaellige_Auswahl_spiel, font=("Arial", 16))
    spielename_label.grid (row=1, column=0)

    erneut_Ausfuehren (fenster, lambda fenster: Spieleauswahl (fenster, liste), spielename_label)
    
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


WoW_Auswahlliste = ["Krieger", "Magier", "Paladin", "Jäger", "Schurke", "Priester", 
                    "Schamane", "Hexenmeister", "Mönch", "Druide", "Dämonenjäger", 
                    "Todesritter", "Rufer"]

Baldurs_Gate_3_Auswahlliste = ["Barbar", "Barde", "Druide", "Hexenmeister", 
                               "Kämpfer", "Kleriker", "Magier", "Mönch", "Paladin", 
                               "Schurke", "Waldläufer", "Zauberer"]

Diablo_4_Auswahlliste = ["Barbar", "Druide", "Geistgeborener", "Jäger", "Totenbeschwörer", "Zauberer"]
    
Monster_Hunter_Wilds_Rise_World_Auswahlliste = ["Langschwert", "Bogen", "Doppelklingen", "Gewehrlanze", "Großschwert", "schweres Bogengewehr",
                                                "Energieklinge", "Jagdhorn", "Schwert und Schild", "Morph-Axt", "leichtes Bogengewehr",
                                                "Hammer", "Insektengleve", "Lanze"]

Wild_Hearts_Auswahlliste = ["Krallenklinge", "Bogen", "Karakuri-Katana", "Nodachi", "Handkanone", "Karakuri-Stab", "Hammer", "Klingen-Wagasa"]

Remnant_2_Auswahlliste = ["Alchemist", "Archon", "Challenger", "Engineer", "Explorer", "Gunslinger", "Handler", "Hunter", "Invader",
                          "Invoker", "Medic", "Summoner", "Ritualist", "Warden"]
    
Last_Epoch_Auswahlliste = ["Mage", "Primalist", "Acolyte", "Rogue", "Sentinel"]

Lords_of_the_Fallen_Auswahlliste = ["Heliger Ritter", "Udirangr-Kriegswolf", "Partisan", "Mournstead-Infanterie", "Schwarzfeder-Waldläufer",
                                    "Verbannter Nachsteller", "Prediger Orius", "Feuerkultist", "Verdammter"]

Oblivion_Auswahlliste = ["Agent", "Akrobat", "Assassine", "Barbar", "Barde", "Bogenschütze", "Dieb", "Heiler", "Hexenjäger", "Hexer", "Kampfmagier",
                         "Kreuzritter", "Krieger", "Kundschafter", "Magier", "Mönch", "Pilger", "Ritter", "Schattenklinge", "Schurke", "Schwertmagier"]

Elden_Ring_Auswahlliste = ["Held", "Bandit", "Astrologe", "Krieger", "Gefangener", "Bekenner", "Bettler", "Vagabund", "Prophet", "Samurai"]

For_the_King_Auswahlliste = ["Schmied", "Jäger", "Minnesänger", "Gelehrter", "Straßenmusiker", "Kräuterkundlerin", "Fallensteller",
                             "Holzfäller", "Hobo", "Mönch", "Schatzsucher", "Astronom", "Gladiator"]

For_the_King_2_Auswahlliste = ["Alchemist", "Schmied", "Straßenmusiker", "Bauer", "Mönch", "Kräuterkundlerin", "Hobo", "Jäger",
                               "Minnesänger", "Pfadfinder", "Gelehrter", "Hirte", "Stallbursche", "Holzfäller", "Spielzeugmacher", "Wahrsager"
                               "Gefallener Ritter", "Leerenwandler", "Imker", "Angler"]

Deep_Rock_Galactic_Auswahlliste = ["Ingenieur", "Schütze", "Bohrer", "Späher"]

Terraria_Auswahlliste = ["Nahkämpfer", "Magier", "Fernkämpfer", "Beschwörer"]
    
Dragons_Dogma_2_Auswahlliste = ["Kämpfer", "Bogenschütze", "Magier", "Dieb", "Krieger", "Magiebogenschütze", "mystische Klinge",
                                "Erzmagier", "Illusionist", "Kriegsmeister"]

Divinity_Original_Sin_2_Auswahlliste = ["Hexe", "Zauberer", "Kampfmagier", "Beschwörer", "Verzauberer", "Kämpfer", "Inquisitor", "Metamorph",
                                        "Ritter", "Kleriker", "Schattenklinge", "Schurke", "Waldläufer", "Wildling"]

Shakes_and_Fidget_Auswahlliste = ["Paladin", "Druide", "Berserker", "Magier", "Kundschafter", "Kampfmagier", "Assassine", "Krieger",
                                  "Dämonenjäger", "Barde", "Nekromant"]
    
Borderlands_4_Auswahlliste = ["Amon", "Harlowe", "Rafa", "Vex"]

Fallout_76_Auswahlliste = ["Pistolen", "nicht-automatisches Gewehr", "vollautomatisches Gewehr", "Bogen / Armbrust", "Shotguns", "schwere Waffen", "explosive Gewehre",
                           "einhand Nahkampf", "zweihand Nahkampf", "Faustwaffen"]

Warhammer_Vermintide_2_Auswahlliste = ["Bardin Goreksson", "Kerillian", "Victor Saltzbrand", "Markus Kruber", "Sienna Fuegonasus"]

Dark_Souls_Auswahlliste = ["Krieger", "Ritter", "Vagabund", "Dieb", "Bandit", "Jäger", "Zauberer", "Pyromant", "Kleriker", "Bettler"]

Dark_Souls_2_Auswahlliste = ["Krieger", "Ritter", "Schwertkämpfer", "Bandit", "Kleriker", "Zauberer", "Erkunder", "Bettler",]

Dark_Souls_3_Auswahlliste = ["Ritter", "Söldner", "Krieger", "Herold", "Dieb", "Assassine", "Zauberer", "Pyromant", "Kleriker", "Bettler"]
   
Destiny_2_Auswahlliste = ["Warlock", "Jäger", "Titan"]

The_Elder_Scrolls_Online_Auswahlliste = ["Drachenritter", "Zauberer", "Nachtklinge", "Hüter", "Nekromant", "Templer", "Arkanist"]

SWTOR_Auswahlliste = ["Jedi-Botschafter", "Imperialer Agent", "Jedi-Ritter", "Kopfgeldjäger", "Schmuggler", "Sith-Inquisitor", "Soldat", "Sith-Krieger"]

Final_Fantasy_XIV_Auswahlliste = ["Paladin", "Krieger", "Dunkelritter", "Revolverklinge", "Weißmagier", "Gelehrter", "Astrologe", "Weiser", "Mönch",
                                  "Dragoon", "Ninja", "Samurai", "Schnitter", "Viper", "Barde", "Maschinist", "Tänzer", "Schwarzmagier",
                                  "Beschwörer", "Rotmagier", "Piktomant", "Blaumagier"]

Dragons_Dogma_Auswahlliste = ["Kämpfer", "Magier", "Streicher", "Krieger", "Erzmagier", "Waldläufer", "Assassine", "Mystischer Ritter", "Magischer Bogenschütze"]

Barony_Auswahlliste = ["Barbarian", "Warrior", "Healer", "Rogue", "Wizard", "Merchant", "Cleric", "Wanderer", "Arcanist", "Joker", "Sexton", "Ninja", "Mesmer", "Accursed",
                       "Conjurer", "Monk", "Brewer", "Mechanist", "Punisher", "Shaman", "Hunter"]

Pathfinder_Wrath_of_the_Righteous_Auswahlliste = ["Alchemist", "Arcanist", "Barbarian", "Bard", "Bloodrager", "Cavalier", "Cleric", "Druid", "Fighter", "Hunter",
                                                  "Inquisitor", "Kineticist", "Magus", "Monk", "Oracle", "Paladin", "Ranger", "Rogue", "Shaman", "Shifter", "Skald",
                                                  "Slayer", "Sorcerer", "Warpriest", "Witch", "Wizard"]
    
Monster_Hunter_Stories_2_Auswahlliste = ["Großschwert, Hammer, Bogen", "Großschwert, Hammer, Gewehrlanze", "Großschwert, Jagdhorn, Bogen", "Großschwert, Jagdhorn, Gewehrlanze",
                                         "Schwert&Schild, Hammer, Bogen", "Schwert&Schild, Hammer, Gewehrlanze", "Schwert&Schild, Jagdhorn, Bogen", "Schwert&Schild, Jagdhorn, Gewehrlanze"]

Borderlands_3_Auswahlliste = ["Amara", "Zane", "FL4K", "Moze"]

Broderlands_2_Auswahlliste = ["Axton", "Salvador", "Maya", "Zero", "Gaige", "Krieg"]

Guild_Wars_2_Auswahlliste = ["Mesmer", "Wächter", "Nekromant", "Waldläufer", "Elementarmagier", "Krieger", "Dieb", "Ingenieur", "Wiedergänger"]

The_Outer_Worlds_Auswahlliste = ["Einhänder Nahkampf", "Zweihänder Nahkampf", "Handfeuerwaffen", "Langwaffen", "Schwere Waffen"]

The_Outer_Worlds_2_Auswahlliste = ["Einhänder Nahkampf", "Zweihänder Nahkampf", "Handfeuerwaffen", "Langwaffen", "Schwere Waffen", "Wissenschaftswaffen"]

Dota_2_Auswahlliste = ["Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe", "Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster",
                       "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen", "Clinkz", "Clockwerk", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dawnbreaker",
                       "Dazzle", "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger", "Earth Spirit", "Earthshaker", "Elder Titan", "Ember Spirit", "Enchantress",
                       "Enigma", "Faceless Void", "Grimstroke", "Gyrocopter", "Hoodwink", "Huskar", "Invoker", "IO", "Jakiro", "Juggernaut", "Keeper of the Light", "Kez", "Kunkka",
                       "Legion Commander", "Leshrac", "Lich", "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan", "Magnus", "Marci", "Mars", "Medusa", "Meepo", "Mirana",
                       "Monkey King", "Morphling", "Muerta", "Naga Siren", "Nature's Prophet", "Necrophos", "Night Stalker", "Nyx Assassin", "Ogre Magi", "Omniknight", "Oracle",
                       "Outworld Destroyer", "Pangolier", "Phantom Assassin", "Phantom Lancer", "Phoenix", "Primal Beast", "Puck", "Pudge", "Pugna", "Queen of Pain", "Razor",
                       "Riki", "Ringmaster", "Rubick", "Sand King", "Shadow Demon", "Shadow Fiend", "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark", "Snapfire",
                       "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit", "Sven", "Techies", "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker", "Tiny",
                       "Treant Protector", "Troll Warlord", "Tusk", "Underlord", "Undying", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Visage", "Void Spirit", "Warlock",
                       "Weaver", "Windranger", "Winter Wyvern", "Witch Doctor", "Wraith King", "Zeugs"]

Tainted_Grail_Fall_of_Avalon_Auswahlliste = ["Ich war unterwegs, um mich zur Armee zu melden", "Ich war auf der Jagd", "Ich habe mich vor der Stadtwachen versteckt", 
                                             "Ich war auf der Suche nach einer alten Kultstätte", "Schweigen"]