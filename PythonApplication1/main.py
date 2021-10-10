""" Programme apprentissage python"""
import pygame

#On importe les fichiers player.py et game.py et la librairie pygame

from game import game
from player import player

if __name__ == '__main__':
    pygame.init()
    game = game()
    game.run()

# Variable string(str) chaine de caractere
# Variable float(float) numérique nombre a virgule
# Variable integer(int) nombre entier
# Variable boolean(bool) Vrai/Faux exemple = age >= 18 (si superieur a 18 retourne true sinon false)
# exemple = "" variable vide
# exemple = 1 ceci est une variable locale
# global exemple ceci est une variable globale
# if = si
# elif = sinon si
# boucle for = pour
# range = dans l' ensemble
# try = essaye except = si sa ne marche pas eception else = si sa marche (try except else dans l' ordre)
# while = boucle tant que, while not == tant que nest pas egal and = et or = ou
# break = arretez une boucle
# type() affiche la classe de la variable (String,object etc)
# def exemple(): on crée une fonction
# exemple(ici on peut mettre un parametre) on apelle la fonction
# return exemple de variable stocker dans une fonction
# exemple = exemple() on apelle la variable retourner dans la fonction pour l' utiliser en dehors d' une fonction
# print("Pour informations la valeur de pi est " + str(pi))
# Ceci est un commentaire """ Ouverture/Fermeture d' un commentaire sur plusieurs ligne """

Helloworld = "Python World"
nom = ""
age = ""
user = ""
taille = ""

def demander_user():
    global user
    while user == "":
        user = input("Veuillez entrez votre nom d' utilisateur pour vous connectez :")

def demander_pass():
    motdepass = ""
    while not motdepass == "admin": # Ici on utilisera un mot de pass par defaut admin parametrable plus tard
        motdepass = input("Veuillez entrez votre mot de pass pour vous connectez (admin) :")
        try:
           motdepass == "admin"
        except:
            print("Erreur : Mot de pass eronner .")
    print("Le mot de pass " + motdepass + " est correct ! Connection en cours ...")
    return motdepass

def demander_nom():
    global nom
    while nom == "":    # Rajouter une vérification prenom en lettre et pas en chiffre
        nom = input("Quel est ton prénom ? ")
        try:
            nom == ""
        except:
            print("Erreur : Vous devez rentrez votre prénom en entier !")
    print("Votre prénom est " + nom)

def demander_age():
    global age
    while age == "":
        age = input("Quel est votre age ? ")
        try:
            age_prochain = int(age) + 1
        except:
            print("Erreur : Vous devez rentrez votre vrai age !")
    while int(age) >= 1 and (int(age)<= 110):
        print("Vous avez " + age + " ans")
        print("L'an prochain vous aurez " + str(age_prochain) + " ans .")
        break
        demander_user()
    while int(age) <= 0 or (int(age)>= 100):
        print("Vous avez mentit sur votre age vous dites avoir " + age + "ans ?")
        break
        demander_age()

def mineur_majeur():
    conditionage = int(age) > 18
    if conditionage and int(age) < 50:
        print ("Vous avez plus de 18 ans vous êtes majeur .")
    elif int(age) < 18 and int(age) > 10:
        print ("Vous avez moins de 18 ans vous êtes mineur .")
    if int(age) == 18:
        print ("Vous avez tout juste 18 ans .")
    if int(age) >= 50:
        print ("Vous avez 50 ans ou plus vous êtes un senior !")
    if int(age) <= 10:
        print ("Vous avez 10 ans ou moins vous êtes un enfant .")
    if int(age) == 1:
        print ("Vous avez 1 an vous êtes un enfant .")
    if int(age) == 2:
        print ("Vous avez 1 an vous êtes un enfant .")
    return conditionage

def taille():
    global taille
    while taille == "":
        taille = input("Quel est votre taille ? ")
        try:
            taille == ""
        except:
            print("Erreur : Vous devez rentrez votre taille !")
    print("Votre taille est de " + str(taille) + " m")

def systemactivate():
    for i in range(1, 4):
        print("Noyau" + (i))

demander_user()
motdepass = demander_pass()
demander_nom()
demander_age()
conditionage = mineur_majeur()
taille()
print("Bienvenue dans votre programme " + Helloworld + " " + nom + " ! ")
print("Activation du systeme ..")
systemactivate()
print("Systeme activer choisissez une option :")
options()
def options():
    print("1.")
    print("2.")
    print("3.")
    print("4. Quittez le programme.")
    global choice
    while choice == "":
        choice = input("Choisissez une option .")
        try:
            choice = ""
        except:
            print("Erreur : Vous devez choisir une option !")
            while choice == 1:
                while choice == 2:
                    while choice == 3:
                        while choice == 4:
                            quit()