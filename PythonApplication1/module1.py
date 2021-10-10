#Appel de la bibliothèque
from tkinter import *
#-------------Création de l'interface graphique---------------
#Création de la fenêtre et de son titre
window = Tk()
window.title("Python 3.9.10")
window.geometry("480x360")
window.minsize(480, 360)
window.mainloop()
user = ""
#Mise en place d'un widget de label
def demander_user():
    global user
    while user == "":
        user = Label(window, text="Veuillez entrez votre nom d' utilisateur :")
        user.pack()
        #Mise en place d'un widget de saisie
        userenter = StringVar()
        userenter.set("")
        userenter2 = Entry(window, textvariable=userenter, width=12)
        userenter2.pack()
        #Mise en place d'un widget de bouton
        boutonuser = Button(window, text="Valider", width=10)
        boutonuser.pack()
        demander_user()