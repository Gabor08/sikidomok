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
filename = PhotoImage(file = "./kellekek/MPP+LOGO-12.png")
background_label = Label(foablak, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
menusor=Frame(foablak)
menusor.pack(side=TOP, fill=X)
menu1=Menubutton(menusor, text='Négyzet', underline=0)
menu1.pack(side=LEFT)
Szam1=Menu(menu1)
Szam1.add_command(label='Számítás', command='',  underline=0)
menu1.config(menu=Szam1)
menu2=Menubutton(menusor, text='Téglalap', underline=0)
menu2.pack(side=LEFT)
Szam2=Menu(menu2)
Szam2.add_command(label='Számítás', command='',  underline=0)
menu2.config(menu=Szam2)
menu3=Menubutton(menusor, text='Háromszög', underline=0)
menu3.pack(side=LEFT)
Szam3=Menu(menu3)
Szam3.add_command(label='Számítás', command='',  underline=0)
menu3.config(menu=Szam3)
menu4=Menubutton(menusor, text='Trapéz', underline=0)
menu4.pack(side=LEFT)
Szam4=Menu(menu4)
Szam4.add_command(label='Számítás', command='',  underline=0)
menu4.config(menu=Szam4)
menu5=Menubutton(menusor, text='Paralelogramma', underline=0)
menu5.pack(side=LEFT)
Szam5=Menu(menu5)
Szam5.add_command(label='Számítás', command='',  underline=0)
menu5.config(menu=Szam5)
menu6=Menubutton(menusor, text='Deltoid', underline=0)
menu6.pack(side=LEFT)
Szam6=Menu(menu6)
Szam6.add_command(label='Számítás', command='',  underline=0)
menu6.config(menu=Szam6)
menu7=Menubutton(menusor, text='Rombusz', underline=0)
menu7.pack(side=LEFT)
Szam7=Menu(menu7)
Szam7.add_command(label='Számítás', command='',  underline=0)
menu7.config(menu=Szam7)
menu8=Menubutton(menusor, text='Kör', underline=0)
menu8.pack(side=LEFT)
Szam8=Menu(menu8)
Szam8.add_command(label='Számítás', command='',  underline=0)
menu8.config(menu=Szam8)

# def vonalatrajzol():
#     x1 =eval(m1.get())
#     y1 =eval(m2.get())
#     x2 =eval(m3.get())
#     y2 =eval(m4.get())
#     vast =eval(m5.get())
#     color =col.get()
#     color2 =col2.get()
#     can1.create_rectangle(x1,y1,x2,y2,width=vast,fill=color,outline=color2)
# can1 = Canvas(foablak,bg='dark grey',height=400,width=400)
# can1.pack(side=RIGHT)
# gomb1 =Button(foablak,text='Kilép',command=foablak.destroy)
# szov1 =Label(foablak,text ='Kitöltési szín:')
# szov1.pack()
# col =StringVar()
# radio1 =Radiobutton(foablak,text='Piros',value='red',variable =col)
# radio2 =Radiobutton(foablak,text='Fehér',value='white',variable =col)
# radio3 =Radiobutton(foablak,text='Zöld',value='green',variable =col)
# radio4 =Radiobutton(foablak,text='Sárga',value='gold',variable =col)
# radio5 =Radiobutton(foablak,text='Kék',value='blue',variable = col)
# radio6 =Radiobutton(foablak,text='Fekete',value='black',variable =col)
# radio1.pack()
# radio2.pack()
# radio3.pack()
# radio4.pack()
# radio5.pack()
# radio6.pack()
# szov2 =Label(foablak,text ='Vonalszín:')
# szov2.pack()
# col2 =StringVar()
# radio7 =Radiobutton(foablak,text='Piros',value='red',variable =col2)
# radio8 =Radiobutton(foablak,text='Vörösesbarna',value='maroon4',variable =col2)
# radio9 =Radiobutton(foablak,text='Zöld',value='green',variable =col2)
# radio10 =Radiobutton(foablak,text='Arany',value='yellow',variable =col2)
# radio11 =Radiobutton(foablak,text='Sötét Orchidea Színű',value='dark orchid',variable =col2)
# radio12 =Radiobutton(foablak,text='Fekete',value='black',variable =col2)
# radio7.pack()
# radio8.pack()
# radio9.pack()
# radio10.pack()
# radio11.pack()
# radio12.pack()
# sz1 =Label(foablak,text ='Vízszintes kezdőpozíció:')
# sz1.pack()
# m1 =Entry(foablak)
# m1.pack()
# sz2 =Label(foablak,text ='Függőleges kezdőpozíció:')
# sz2.pack()
# m2 =Entry(foablak)
# m2.pack()
# sz3 =Label(foablak,text ='Vízszintes végpozíció:')
# sz3.pack()
# m3 =Entry(foablak)
# m3.pack()
# sz4 =Label(foablak,text ='Függőleges végpozíció:')
# sz4.pack()
# m4 =Entry(foablak)
# m4.pack()
# sz5 =Label(foablak,text ='Vonalvastagság:')
# sz5.pack()
# m5 =Entry(foablak)
# m5.pack()
# gomb1.pack(side=BOTTOM)
# gomb2 =Button(foablak,text='Vonalat rajzol',command=vonalatrajzol)
# gomb2.pack()

# vaszon =Canvas(foablak,bg='dark grey',height=400,width=400)
# vaszon.pack(side=LEFT)

foablak.mainloop()