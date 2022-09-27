#Appel de la bibliothèque
import tkinter
from tkinter import *

#-------------Création de l'interface graphique---------------
#Création de la fenêtre et de son titre

window = Tk()
window.title("Hollows Game Helper")
window.geometry("800x600")
window.minsize(800, 600)
window.configure(bg='black')
user = ""
hollow = PhotoImage(file="hollow.jpg")

def create():
    win = Toplevel(window)

#Mise en place des boutons
bouton = tkinter.Button (text = "Database", command= create, bg="white", relief=RAISED, cursor="cross")
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
labeldatabase.place(x=290, y=150)

#Canvas Image
canvas = Canvas(window, width=300, height=200, background='yellow')
canvas.create_image(0, 0, anchor=NW, image=hollow)
canvas.pack()
canvas.place(x=250, y=250)
window.mainloop()