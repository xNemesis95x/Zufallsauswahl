import random
from tkinter import *
from Spieleauswahl import *

fenster = Tk()
fenster.title("Hauptmenü")
fenster.geometry ("800x500")

WoW_Button = Button(fenster, text="WoW", command=lambda:WoW_Auswahl (fenster))
WoW_Button.grid(row=0, column=0)

Zufallsauswahl_Button = Button(fenster, text="Zufallsauswahl aus erstellter Liste", command=lambda:Zufallsauswahl (fenster))
Zufallsauswahl_Button.grid(row=0, column=1)

Baldurs_Gate_3_Button = Button (fenster, text="Baldurs Gate 3", command=lambda:Baldurs_Gate_3_Auswahl (fenster))
Baldurs_Gate_3_Button.grid (row=0, column=2)

Diablo_4_Button = Button (fenster, text="Diablo 4", command=lambda:Diablo_4_Auswahl (fenster))
Diablo_4_Button.grid (row=0, column=3)

Monster_Hunter_Wilds_Rise_World_Button = Button (fenster, text="Monster Hunter Wilds/Rise/World", command=lambda:Monster_Hunter_Wilds_Rise_World_Auswahl (fenster))
Monster_Hunter_Wilds_Rise_World_Button.grid (row=1, column=1)

Wild_Hearts_Button = Button (fenster, text="Wild Hearts", command=lambda:Wild_Hearts_Auswahl (fenster))
Wild_Hearts_Button.grid (row=0, column=4)

Remnant_2_Button = Button (fenster, text="Remnant 2", command=lambda:Remnant_2_Auswahl (fenster))
Remnant_2_Button.grid (row=0, column=5)

Last_Epoch_Button = Button (fenster, text="Last Epoch", command=lambda:Last_Epoch_Auswahl (fenster))
Last_Epoch_Button.grid (row=0, column=6)

Lords_of_the_Fallen_Button = Button (fenster, text="Lords of the Fallen", command=lambda:Lords_of_the_Fallen_Auswahl (fenster))
Lords_of_the_Fallen_Button.grid (row=2, column=1)

Oblivion_Button = Button (fenster, text="Oblivion", command=lambda:Oblivion_Auswahl (fenster))
Oblivion_Button.grid (row=0, column=7)

Elden_Ring_Button = Button (fenster, text="Elden Ring", command=lambda:Elden_Ring_Auswahl (fenster))
Elden_Ring_Button.grid (row=0, column=8)

For_the_King_Button = Button (fenster, text="For the King", command=lambda:For_the_King_Auswahl (fenster))
For_the_King_Button.grid (row=0, column=8)

For_the_King_2_Button = Button (fenster, text="For the King 2", command=lambda:For_the_King_2_Auswahl (fenster))
For_the_King_2_Button.grid (row=1, column=8)

Jotunnslayer_Button = Button (fenster, text="Jotunnslayer", command=lambda:Jotunnslayer_Auswahl (fenster))
Jotunnslayer_Button.grid (row=1, column=2)

fenster.mainloop()
