""" Programme apprentissage python"""

# Variable string(str) chaine de caractere
# Variable float(float) numérique nombre a virgule
# Variable integer(int) nombre entier
# Variable boolean(bool) True/False
# exemple = "" variable vide
# exemple = 1 ceci est une variable locale
# try = essaye except = si sa ne marche pas else = si sa marche
# while = boucle tant que, while not == tant que nest pas egal and = et or = ou
# break = arretez une boucle
# type() affiche la classe de la variable (String,object etc)
# global exemple ceci est une variable globale
# def exemple(): on crée une fonction
# exemple(ici on peut mettre un parametre) on apelle la fonction
# return exemple de variable stocker dans une fonction
# exemple = exemple() on apelle la variable retourner dans la fonction pour l' utiliser en dehors d' une fonction
# print("Pour informations la valeur de pi est " + str(pi))
# Ceci est un commentaire """ Ouverture/Fermeture d' un commentaire sur plusieurs ligne """

Helloworld = "Hello World"
print(Helloworld)
nom = ""
age = ""
user = ""
pi = 3.14
def demander_nom():
    global nom
    while nom == "":
        nom = input("Quel est ton nom ? ")
    print("Votre nom est " + nom)
def demander_age():
    global age
    while age == "":
        age = input("Quel est votre age ? ")
        try:
            age_prochain = int(age) + 1
        except:
            print("Erreur : Vous devez rentrez votre vrai age !")
    while int(age) >= 1 and (int(age)<= 110) :
        print("Vous avez " + age + " ans")
        print("L'an prochain vous aurez " + str(age_prochain) + " ans .")
        break
        demander_user()
    while int(age) <= 0 or (int(age)>= 111) :
        print("Vous avez mentit sur votre age vous dites avoir " + age + "ans ?")
        break
        demander_age()
def demander_user():
    global user
    while user == "":
        user = input("Veuillez entrez votre nom d' utilisateur pour vous connectez :")
    print("Votre nom d' utilisateur est " + user)
def demander_pass():
    motdepass = ""
    while not motdepass == "admin":
        motdepass = input("Veuillez entrez le mot de pass pour vous connectez :")
        try:
           motdepass == "admin"
        except:
            print("Mot de pass eronner .")
    print("Le mot de pass " + motdepass + " est correct ! Connection en cours ...")
    return motdepass
demander_nom()
demander_age()
demander_user()
motdepass = demander_pass()
print("Bienvenue dans votre programme Hello World .")