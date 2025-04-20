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

fenster.mainloop()