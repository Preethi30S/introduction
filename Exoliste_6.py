
# Exercices sur les listes

#Exo cours

l1=[1,1,2,3,5,8]
l2=["un","deux","trois"]
l3=[1,2,3,4,"trois"]

l1[3]=5
print(l1)
"""a=l1[2]#pour stocker
print(a)"""

print(len(l3))
print("+++++++++++++++++")

"""Définir une fonction qui prend en paramètre une liste et qui retourne son 5e élément. 
Tester cette fonction sur plusieurs listes. Que se passe-t-il si la liste est trop courte?"""

def f2 (liste):
    return liste[4] #Rappel: les indices commencent à 0 donc le 5e élément est d'indice 4.

print(f2(l1))
print(f2(l3))
#print(f2(l2)) # si la liste est courte, cela donne une erreur type "index out of range"

"""A l’aide de deux boucles, définir une liste qui contient 5 fois l’élément False, une fois l’élément True puis trois fois l’élément False."""

lplace=[]
for place in range(5):
    lplace.append(False)
lplace.append(True)
for place in range(3):
    lplace.append(False)
print(lplace)

"""Définir une fonction qui prend une chaîne de caractères en argument (c’est-à-dire en paramètre) et affiche 3 fois sa toisième lettre. 
Comment faire pour afficher 3 fois sa dernière lettre ? (vous aurez sans doute besoin de voir la documentation python officielle 
sur les listes)"""

# affiche 3eme lettre 3 fois
s= "preethi"
def f3 (CdC):
    print(3*CdC[2])
f3 (s)
# affiche derniere lettre 3 fois
def f4 (CdC):
    print(3*CdC[len(CdC)-1]) # ou print(3*CdC[-1])
f4 (s)

"""Les éléments d’une liste peuvent être de tout type. Ils peuvent même être des listes. Créer et afficher une liste de 10 éléments, 
chaque élément étant une liste de 4 éléments."""

l10=[]
for idx in range(10):
    l10.append([1,2,3,4])
print(l10)

"""Créer la variable table_multiplication qui est une liste de listes telle que table_multiplication[i][j] est un nombre égal au produit 
de i et de j."""

table_multiplication=[]
num_table=5 #jusqu'au 4e table.
for idx in range(num_table):
   table_multiplication.append([0 for i in range(11)])   #table_multiplication.append([0,0,0,0,0,0,0,0,0,0,0])
for i in range (num_table):
    for j in range(11):
        table_multiplication[i][j]=i*j
print(table_multiplication)




