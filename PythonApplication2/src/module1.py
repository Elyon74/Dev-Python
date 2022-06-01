#Appel de la bibliothèque
from tkinter import *

#-------------Création de l'interface graphique---------------
#Création de la fenêtre et de son titre

window = Tk()
window.title("Python 3.10.4")
window.geometry("640x480")
window.minsize(640, 480)
window.configure(bg='red')
window.mainloop()
user = ""

#Mise en place d'un widget de label (fenetre du programme)