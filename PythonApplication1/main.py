""" Programme apprentissage python"""

# Variable string(str) chaine de caractere
# Variable float(float) numérique nombre a virgule
# Variable integer(int) nombre entier
# Variable boolean(bool) True/False
# try = essaye except = si sa ne marche pas else = si sa marche
# while = boucle tant que, while not == tant que nest pas egal
# type() affiche la classe de la variable (String,object etc)
# Ceci est un commentaire """ Ouverture/Fermeture d' un commentaire sur plusieurs ligne """

Helloworld = "Hello World"
print(Helloworld)
pi = 3.14
motdepass = ""
nom = input("Quel est ton nom ? ")
try:
    nomentrer = str(nom)
except:
    print("Erreur : Vous devez rentrez un nom .")
else:
    age = input("Quel est votre age ? ")
try:
    age_prochain = int(age) + 1
except:
    print("Erreur : Vous devez rentrez votre vrai age !")
else:
    print("Votre nom est " + nom)
while age <=110:
    while age >=1:
        print("Vous avez " + age + " ans")
while age >=111:
    print("Vous avez mentit sur votre age vous dites avoir plus de " + age + "ans ?")
    while age <=0 :
        print ("Vous avez mentit sur votre age vous dites avoir plus de " + age + "ans ?")
print("L' an prochain vous aurez " + str(age_prochain) + " ans .")
print("Pour informations la valeur de pi est " + str(pi))
while not motdepass == "admin":
    motdepass = input("Veuillez entrez le mot de pass pour vous connectez :")
print("Le mot de pass est correct ! connection en cours ...")
print ("Merci, passez une bonne journée")