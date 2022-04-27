#Síkidomok v0.1
from tkinter import *

foablak = Tk()
foablak.title("Síkidomok")
foablak.geometry("1024x768")
abl_szelesseg = 1024
abl_magassag = 768
kep_szelesseg = foablak.winfo_screenwidth()
kep_magassag = foablak.winfo_screenheight()
center_x = int(kep_szelesseg/2 - abl_szelesseg / 2)
center_y = int(kep_magassag/2 - abl_magassag / 2)
foablak.resizable(False, False)
foablak.iconphoto(True, PhotoImage(file='./kellekek/negyzetikon.png'))


foablak.mainloop()
