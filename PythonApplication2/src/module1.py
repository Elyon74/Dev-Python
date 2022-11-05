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
    boutonboss = tkinter.Button (win, text = "Boss/Ennemies", command= create6, bg="red", relief=RAISED, cursor="cross")
    labeldatabaseboss = Label(win, text="Liste des Boss/Ennemies")
    labeldatabaseboss.pack ()
    labeldatabaseboss.place(x=300, y=250)
    boutonlieu = tkinter.Button (win, text = "Lieu", command= create7, bg="red", relief=RAISED, cursor="cross")
    labeldatabaselieu = Label(win, text="Liste des lieu")
    labeldatabaselieu.pack ()
    labeldatabaselieu.place(x=250, y=285)
    boutonexit = tkinter.Button (win, text = "Quitter la database", command=win.destroy, bg="red", relief=RAISED, cursor="cross")
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
    boutonboss.pack()
    boutonboss.place(x=200, y=250)
    boutonlieu.pack()
    boutonlieu.place(x=200, y=285)
    boutonexit.pack ()
    boutonexit.place(x=340, y=340)

# Database
def create1():
    win1 = Toplevel(window)
    win1.title("Hollows Game Helper (Armes)")
    win1.geometry("950x600")
    win1.minsize(950, 600)
    win1.resizable(height=False, width=False)
    win1.configure(bg='black')
    labelweapon = Label(win1, text="Liste des armes :", bg="white", font="Arial 15 bold")
    labelweapon.pack ()
    labelweapon.place(x=50, y=30)
    labelweaponlist = Label(win1, text=" Épée courte\n Épée longue\n Sabre\n Épée en mithril\n Lame du dragon\n Bâton de feu\n Bâton magique\n Bâton de force\n Bâton en mithril\n Bâton du dragon\n Fléau en pierre\n Fléau en bronze\n Morgenstern\n Fléau en mithril\n Fléau du dragon\n Hachette\n Hache de combat\n Bardiche\n Hache en mithril\n Hache du dragon\n Lance courte\n Lance longue\n Hallebarde\n Lance en mithril\n Lance du dragon\n Ceste\n Griffes de tigre\n Griffes de fer\n Griffes en mithril\n Griffes du dragon\n", bg="black", foreground="white", font="Arial 10 bold")
    labelweaponlist.pack ()
    labelweaponlist.place(x=50, y=70)
    labelweaponlist2 = Label(win1, text="Arc court\n Arc long\n Arbalète\n Arbalète en mithril\n Arc du dragon\n Couteau\n Dague\n Machette\n Dague en mithril\n Dague du dragon", bg="black", foreground="white", font="Arial 10 bold")
    labelweaponlist2.pack ()
    labelweaponlist2.place(x=450, y=70)
    labelweaponstat = Label(win1, text ="Une épée à lame courte légère à manier. +8 ATQ\n Une épée à lame longue et tranchante. +12 ATQ\n Une épée large à lame courbée. +18 ATQ\n",bg="black", foreground="white", font="Arial 8 bold")
    labelweaponstat.pack ()
    labelweaponstat.place(x=180, y=70)
    boutonexitwin1 = tkinter.Button(win1, text = "Fermez la fenetre", command=win1.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin1.pack ()
    boutonexitwin1.place(x=400, y=480)

def create2():
    win2 = Toplevel(window)
    win2.title("Hollows Game Helper (Equipements)")
    win2.geometry("950x600")
    win2.minsize(950, 600)
    win2.resizable(height=False, width=False)
    win2.configure(bg='black')
    boutonexitwin2 = tkinter.Button(win2, text = "Fermez la fenetre", command=win2.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin2.pack ()
    boutonexitwin2.place(x=400, y=480)

def create3():
    win3 = Toplevel(window)
    win3.title("Hollows Game Helper (Accesoires)")
    win3.geometry("950x600")
    win3.minsize(950, 600)
    win3.resizable(height=False, width=False)
    win3.configure(bg='black')
    boutonexitwin3 = tkinter.Button(win3, text = "Fermez la fenetre", command=win3.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin3.pack ()
    boutonexitwin3.place(x=400, y=480)

def create4():
    win4 = Toplevel(window)
    win4.title("Hollows Game Helper (Chimère)")
    win4.geometry("950x600")
    win4.minsize(950, 600)
    win4.resizable(height=False, width=False)
    win4.configure(bg='black')
    canvas = Canvas(win4, width=100, height=100)
    canvas.pack()
    img=ImageTk.PhotoImage(file="D:\Anthony\Documents\Dev Python\PythonApplication2\ifrit.jpg")
    canvas.image = img
    canvas.create_image(100/2,100/2,image=img, anchor=CENTER)
    canvas.place(x=100, y=120)
    labelchimeralist = Label(win4, text="Liste des chimères :", bg="white", font="Arial 15 bold")
    labelchimeralist.pack ()
    labelchimeralist.place(x=50, y=30)
    labelchimera = Label(win4, text=" Ifrit la chimère du feu s' obtient au volcan de l' ifrit .", bg="black", foreground="red", font="Arial 10 bold")
    labelchimera.pack ()
    labelchimera.place(x=50, y=100)
    boutonexitwin4 = tkinter.Button(win4, text = "Fermez la fenetre", command=win4.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin4.pack ()
    boutonexitwin4.place(x=400, y=480)

def create5():
    win5 = Toplevel(window)
    win5.title("Hollows Game Helper (Objects)")
    win5.geometry("950x600")
    win5.minsize(950, 600)
    win5.resizable(height=False, width=False)
    win5.configure(bg='black')
    boutonexitwin5 = tkinter.Button(win5, text = "Fermez la fenetre", command=win5.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin5.pack ()
    boutonexitwin5.place(x=400, y=480)

def create6():
    win6 = Toplevel(window)
    win6.title("Hollows Game Helper (Boss/Ennemies)")
    win6.geometry("950x600")
    win6.minsize(950, 600)
    win6.resizable(height=False, width=False)
    win6.configure(bg='black')
    boutonexitwin6 = tkinter.Button(win6, text = "Fermez la fenetre", command=win6.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin6.pack ()
    boutonexitwin6.place(x=400, y=480)

def create7():
    win7 = Toplevel(window)
    win7.title("Hollows Game Helper (Lieu)")
    win7.geometry("950x600")
    win7.minsize(950, 600)
    win7.resizable(height=False, width=False)
    win7.configure(bg='black')
    boutonexitwin7 = tkinter.Button(win7, text = "Fermez la fenetre", command=win7.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitwin7.pack ()
    boutonexitwin7.place(x=400, y=480)

def menue():
    menue = Toplevel(window)
    menue.title("A propos")
    menue.geometry("200x100")
    menue.minsize(230, 100)
    menue.resizable(height=False, width=False)
    menue.configure(bg='white')
    labelmenue = Label(menue, text="Version 0.1", bg="white", font="Arial 15 bold")
    labelmenue.pack ()
    labelmenue.place(x=60, y=25)
    boutonexitmenue = tkinter.Button(menue, text = "Fermez la fenetre", command=menue.destroy, bg="red", relief=RAISED, cursor="cross")
    boutonexitmenue.pack ()
    boutonexitmenue.place(x=60, y=60)

#Mise en place des boutons
bouton = tkinter.Button (text = "Database", command= create, bg="yellow", relief=RAISED, cursor="cross")
boutonexit = tkinter.Button (text = "Quitter le logiciel", command=window.quit, bg="red", relief=RAISED, cursor="cross")
bouton.pack ()
bouton.place(x=370, y=100)
boutonexit.pack ()
boutonexit.place(x=350, y=200)

#Case a cocher
checkbox = Checkbutton(window, text="Version complète", bg ="black", foreground="white", relief=RAISED, cursor="cross")
checkbox.pack()
checkbox.place(x=450, y=100)

#Texte du logiciel
labeldatabase = Label(window, text="Découvrez la database officielle du jeux !")
labeldatabase.pack ()
labeldatabase.place(x=285, y=135)
labelspoiler = Label(window, text="ATTENTION SPOILER !", bg="red")
labelspoiler.pack()
labelspoiler.place(x=335, y=165)
labelgameversion = Label(window, text="Version actuelle du jeu : 0.1", bg="black", foreground="white")
labelgameversion.pack()
labelgameversion.place(x=575, y=525)
labeldatabaseversion = Label(window, text="Version actuelle de la database : 0.1", bg="black", foreground="white")
labeldatabaseversion.pack()
labeldatabaseversion.place(x=575, y=550)

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