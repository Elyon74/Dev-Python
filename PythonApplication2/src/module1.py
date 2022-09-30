#Appel de la bibliothèque
import tkinter
from tkinter import *
from PIL import Image, ImageTk

#-------------Création de l'interface graphique---------------
#Création de la fenêtre et de son titre

window = Tk()
window.title("Hollows Game Helper")
window.geometry("800x600")
window.minsize(800, 600)
window.resizable(height=False, width=False)
window.configure(bg='black')
user = ""
width = 300
height = 300
hollow = Image.open("hollow.jpg")
hollow = hollow.resize((width,height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(hollow)

def create():
    win = Toplevel(window)
    win.title("Hollows Game Helper (Database)")
    win.geometry("800x600")
    win.minsize(800, 600)
    win.resizable(height=False, width=False)
    win.configure(bg='black')
    #Mise en place des boutons
    boutonweap = tkinter.Button (win, text = "Armes", command= create1, bg="red", relief=RAISED, cursor="cross")
    labeldatabaseweapon = Label(win, text="Liste des armes")
    labeldatabaseweapon.pack ()
    labeldatabaseweapon.place(x=285, y=100)
    boutonarm = tkinter.Button (win, text = "Equipements", command= create2, bg="red", relief=RAISED, cursor="cross")
    labeldatabasearm = Label(win, text="Liste des équipements")
    labeldatabasearm.pack ()
    labeldatabasearm.place(x=285, y=130)
    boutonacc = tkinter.Button (win, text = "Accessoires", command= create3, bg="red", relief=RAISED, cursor="cross")
    labeldatabaseacc = Label(win, text="Liste des accessoires")
    labeldatabaseacc.pack ()
    labeldatabaseacc.place(x=285, y=160)
    boutonchim = tkinter.Button (win, text = "Chimère", command= create4, bg="red", relief=RAISED, cursor="cross")
    labeldatabasechim = Label(win, text="Liste des chimère")
    labeldatabasechim.pack ()
    labeldatabasechim.place(x=285, y=190)
    boutonobj = tkinter.Button (win, text = "Objects", command= create5, bg="red", relief=RAISED, cursor="cross")
    labeldatabaseobj = Label(win, text="Liste des objects")
    labeldatabaseobj.pack ()
    labeldatabaseobj.place(x=285, y=220)
    boutonexit = tkinter.Button (win, text = "Quitter le logiciel", command=window.quit, bg="red", relief=RAISED, cursor="cross")
    boutonweap.pack ()
    boutonweap.place(x=200, y=100)    
    boutonarm.pack ()
    boutonarm.place(x=200, y=130)
    boutonacc.pack ()
    boutonacc.place(x=200, y=160)
    boutonchim.pack ()
    boutonchim.place(x=200, y=190)
    boutonobj.pack ()
    boutonobj.place(x=200, y=220)
    boutonexit.pack ()
    boutonexit.place(x=340, y=270)

def create1():
    win1 = Toplevel(window)
    win1.title("Hollows Game Helper (Armes)")
    win1.geometry("800x600")
    win1.minsize(800, 600)
    win1.resizable(height=False, width=False)
    win1.configure(bg='black')

def create2():
    win2 = Toplevel(window)
    win2.title("Hollows Game Helper (Equipements)")
    win2.geometry("800x600")
    win2.minsize(800, 600)
    win2.resizable(height=False, width=False)
    win2.configure(bg='black')

def create3():
    win3 = Toplevel(window)
    win3.title("Hollows Game Helper (Accesoires)")
    win3.geometry("800x600")
    win3.minsize(800, 600)
    win3.resizable(height=False, width=False)
    win3.configure(bg='black')

def create4():
    win4 = Toplevel(window)
    win4.title("Hollows Game Helper (Chimère)")
    win4.geometry("800x600")
    win4.minsize(800, 600)
    win4.resizable(height=False, width=False)
    win4.configure(bg='black')

def create5():
    win5 = Toplevel(window)
    win5.title("Hollows Game Helper (Objects)")
    win5.geometry("800x600")
    win5.minsize(800, 600)
    win5.resizable(height=False, width=False)
    win5.configure(bg='black')

def menue():
    menue = Toplevel(window)
    menue.title("A propos")
    menue.geometry("200x100")
    menue.minsize(230, 100)
    menue.resizable(height=False, width=False)
    menue.configure(bg='white')
    labelmenue = Label(menue, text="Version 0.1", bg="white", font="Arial 15 bold")
    labelmenue.pack ()
    labelmenue.place(x=60, y=40)

#Mise en place des boutons
bouton = tkinter.Button (text = "Database", command= create, bg="yellow", relief=RAISED, cursor="cross")
boutonexit = tkinter.Button (text = "Quitter le logiciel", command=window.quit, bg="red", relief=RAISED, cursor="cross")
bouton.pack ()
bouton.place(x=370, y=100)
boutonexit.pack ()
boutonexit.place(x=350, y=200)

#Case a cocher
checkbox = Checkbutton(window, text="Version simplifier", bg ="black", foreground="white", relief=RAISED, cursor="cross")
checkbox.pack()
checkbox.place(x=450, y=100)

#Texte du logiciel
labeldatabase = Label(window, text="Découvrez la database officielle du jeux !")
labeldatabase.pack ()
labeldatabase.place(x=285, y=150)

#Image
label1 = tkinter.Label(image=image)
label1.image = image

#Position image
label1.place(x=250, y=250)

#Barre de menue

menubar = tkinter.Menu(window)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="A propos", command = menue)
menubar.add_cascade(label="Options", menu=filemenu)
window.config(menu=menubar)
window.mainloop()