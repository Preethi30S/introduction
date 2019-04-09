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
#Implémenter une fonction qui afficher un nombre s’il est inférieur à 10, ne fait rien sinon.

def f1(x):
    if x<10:
        print(x)
f1(0)

#EXO 4
"""Implémenter une fonction qui prend en argument un nombre compris entre 0 et 9. Cette fonction renvoie ce nombre plus un, 
sauf si le nombre vaut 9 auquel cas elle renvoie 9. """
def ma_fonction09 (x): # x doit être compris entre O et 9.
    if 0<=x and x<=8:
        return x+1
    else:
        return 9
print('yes', ma_fonction09(0))
print('non', ma_fonction09(9))

#EX0 5
#Implémenter une fonction qui décrémente un nombre, sauf si ce nombre vaut 0.
def ma_fonctiondecrease (x):
    if x!=0:
        print("decreased", x-1)
ma_fonctiondecrease(0)
ma_fonctiondecrease(6)

#EXO bissextile

def fleapyear (Y):
    if Y % 4==0 and Y % 100 != 0:
        return(True)
    elif Y % 400 == 0:
        return(True)
    else:
        return(False)

print(fleapyear(2000)) #true
print(fleapyear(1900)) #false
print(fleapyear(2048)) #true
print(fleapyear(2019)) #false
print(fleapyear(2020)) #true