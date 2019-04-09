# exercices sur les fonctions

#exemple du cours
def ma_fonction(parametre):
    variable= parametre+3
    return variable
print (ma_fonction(4)) # 1ère méthode
resultat=ma_fonction(5) #2ème méthode qui permet de stocker le résultat.
print (resultat)

# exo double
#Implémenter une fonction qui prend en argument un nombre et renvoie son double.
def ma_fonctiondouble(nombre):
    variable=nombre*2
    return variable
print (ma_fonctiondouble(6))

#Implémenter une fonction qui prend en argument un nombre et affiche son double, mais ne retourne rien.
def ma_fonctiondouble(nombre):
    variable=nombre*2
    print(variable) 
ma_fonctiondouble(2)

#exo longueur
def ma_fonctionlength (l):
    return len(l)
lis=["my","name","is","preethi"]           
print ("longueur " ,ma_fonctionlength(lis))

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
fonction_recursive(10) 
# Que fait f(10) ?  f(10) affiche les entiers de 10 à 1 par ordre décroissant et affiche à la fin "x est nul" car x vaut 0
