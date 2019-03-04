
print(2+2)
print("abc")

#COMMENTAIRES
# print("abc")
"""print("abc")"""

2+2 # ne fait rien puisqu'il n'a pas print

# Que fait l’opérateur % ? il donne le reste de la division euclidienne.

print(18/9) # la réponse est 2.0 (il nous donne un nombre flottant même si on divise 2 nombres entiers entre eux.

# Les boucles (cours)
#ex 1
for counter in range(10):
    print(counter)

for counter in range(5,10):
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

# exercices sur les fonctions

#exemple du cours
def ma_fonction(parametre):
    variable= parametre+3
    return variable

print (ma_fonction(4))

resultat=ma_fonction(5)
print (resultat)

#exo puissance
def ma_fonctionpuissance(a,b):
    return a**b
print (ma_fonctionpuissance(4,2))

#exo recursive
def fonction_recursive(x):
    if x == 0:
        print('x est nul')
    else:
        print(x)
        nouveau_x = x-1
        fonction_recursive(x=nouveau_x)
#print(fonction_recursive(10))
fonction_recursive(10) # f(10) affiche de 10 à 1 et à la fin "x est nul"

#Exercices sur les tests

# EXO COURS 
ma_variable=42
if ma_variable+12<54:
    print("plus petit")
elif ma_variable+12==54:
    print("egaux")
else:
    print("plus grand")

# EXO 2 nombres egaux
ma_variable1=2
ma_variable2=3

if ma_variable1==ma_variable2:
     print("egaux")
else:
     print("ne sont pas egaux")

#EXO 3

def f1(x):
    if x<10:
        print(x)
f1(0)

# Exercices sur les listes

#Exo cours

l1=[1,1,2,3,5,8]
l2=["un","deux","trois"]
l3=[1,2,"trois"]

l1[3]=5
print(l1)
"""a=l1[2]#pour stocker
print(a)"""
print(len(l3))
print("+++++++++++++++++")

# Définir une fonction qui prend en paramètre une liste et qui retourne son 5e élément. Tester cette fonction sur plusieurs listes. Que se passe-t-il si la liste est trop courte ?

def f2 (liste):
    return liste[4]

print(f2(l1))
#print(f2(l2)) # cela donne une erreur type "index out of range"

#Définir une fonction qui prend une chaîne de caractères en argument (c’est-à-dire en paramètre) et affiche 3 fois sa toisième lettre. Comment faire pour afficher 3 fois sa dernière lettre ? (vous aurez sans doute besoin de voir la documentation python officielle sur les listes)

# affiche 3eme lettre 3 fois
def f3 (CdC):
    print(3*CdC[2])

s= "preethi"
f3 (s)

# affiche derniere lettre 3 fois
def f4 (CdC):
    print(3*CdC[len(CdC)-1])

f4 (s)















    
    

    





    
    




