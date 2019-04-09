# Les boucles 
# 2 exos du cours:
#ex 1
for counter in range(10): # affiche les entiers entre 0 et 9 inclus
    print(counter)

for counter in range(5,10): # affiche les entiers de 5 à 9 inclus
    print(counter)

for counter in range(0,11,2): # affiche les nombres paires de 0 à 10 inclus
    print(counter)
#ex 2
liste_les_invites = ["Marcel", "Hippolyte", "Berthe"]
for Chaque_invite in liste_les_invites:
    print("Bienvenu " + Chaque_invite)

 #Afficher les nombres paires entre 0 et 30.   
for counter in range(0,31,2):
    print(counter)
    
#Afficher en ordre décroissant les nombres de 10 à 1.
for counter in range(10,0,-1):
    print(counter)

#Calculer 1 x 2 x 3 x 4 x 5 x 6 avec une boucle.
a=1 #stocker une valeur dans un variable
for counter in range(1,7):
    a=counter*a
   # print(a) donne tous les résultats à chaque itération du boucle
print(a)

"""Avec une boucle imbriquée dans une boucle, afficher le texte suivant. Les mots “Bonjour”, “Comment vas-tu”, “Au revoir”, “Paul”, “Rose”, “Etienne”
ne doivent apparaître qu’une fois chacun dans le code."""

listePER = ["Paul ","Rose ","Etienne "]
listesalutation= ["bonjour ","Comment vas-tu ","Au revoir "]

for chaque_salutation in listesalutation:
    for chaque_personne in listePER:
        print(chaque_salutation +chaque_personne)

for chaque_personne in listePER:
    for chaque_salutation in listesalutation:
        print(chaque_salutation + chaque_personne)

