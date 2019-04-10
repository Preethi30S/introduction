# Problèmes

#P1: Arithmétique alphabétique

# méthode simple
a=1;b=2;c=3;d=4;e=5;f=6;g=7;h=8;i=9;j=10;k=11;l=12;m=13;n=14;o=15;p=16;q=17;r=18;s=19;t=20;u=21;v=22;w=23;x=24;y=25;z=26
print (g+a+r+e+d+a+u+z+t+e+r+l+i+z)
print (c+h+e+v+a+l+e+r+e+t)


#P2 César

    #1 Rechercher ce qu’est le chiffre de César.
    #le chiffrement de César est un décalage des lettres utilisé par Jules César dans ses correspondances secrètes( par exemple, A->D; B->E; C->F ...etc. )

    #2 Chiffrer à la main la phrase “BONJOUR MONDE”.
    # ERQMRXU PRQGH

    #3 Déchiffrer à la main la phrase “DWWDTXHUDOHVLDPDLQWHQDQW”.
    #  Attaquer Alesia maintenant

#4 #Implémenter le chiffrement.
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def chiffrer(texte_a_chiffrer, decalage):
    if decalage > 25:
        print('Erreur ! Decalage trop important')
        return
    texte_chiffre = ''
    for lettre in texte_a_chiffrer:
        if lettre == ' ':
            nouvelle_lettre = ' '
        else:

            mon_index = alphabet.index(lettre)
            nouvel_index = mon_index + decalage

            if nouvel_index >= 26:
                nouvel_index = nouvel_index - 26

            nouvelle_lettre = alphabet[nouvel_index]
        texte_chiffre = texte_chiffre + nouvelle_lettre
    print(texte_chiffre)
"""chiffrer(texte_a_chiffrer="REBONJOUR", decalage=42)
chiffrer(texte_a_chiffrer="BONNE NUIT ZZZ", decalage=1)"""

    #4 Implémenter le déchiffrement
def dechiffrer(texte_a_dechiffrer, decalage):
    if decalage > 25:
        print('Erreur ! Decalage trop important')
        return
    texte_dechiffre = ''
    for lettre in texte_a_dechiffrer:
        if lettre == ' ':
            nouvelle_lettre = ' '
        else:

            mon_index = alphabet.index(lettre)
            nouvel_index = mon_index - decalage

            if nouvel_index >= 26:
                nouvel_index = nouvel_index - 26

            nouvelle_lettre = alphabet[nouvel_index]
        texte_dechiffre = texte_dechiffre + nouvelle_lettre
    print(texte_dechiffre)
#dechiffrer(texte_a_dechiffrer="CPOOF OVJU AAA", decalage=1)
#5
"""bout ="XQOTURRDQPQOEMDRAZOFUAZZQBMDPOMXMSQPQEXQFFDQEPQXMXBTMNQFBMDQJQYBXQPMZEXUYMSQOUPQEEGEUXKMGZQPUEFMZ"
for d in range(1,27):
    dechiffrer(texte_a_dechiffrer=bout,decalage=d)""" # Après avoir testé, je trouve que le décallage est de 12.
  

#P3 Devenir un nombre

#Q1 On utilise:
"""from random import randint
 randint(0,100)"""
"""Q2 Programmer un jeu qui génère alétoirement un nombre, puis demande à l’utilisateur de le deviner en un essai. Le programme indique 
uniquement si le nombre est trop petit, trop grand ou si c’est le nombre à deviner."""
from random import randint
variable_aleatoire=randint(0,100)
nombre_sring=input("entrer un nombre entre 0 et 100: ")
nbr=int(nombre_sring)
if nbr<variable_aleatoire:
    print("trop petit")
elif nbr>variable_aleatoire:
    print("trop grand")
else:
    print("nombre a deviner")
#Q3 Même question mais l’utilisateur dispose de 6 essais. S’il a deviné le nombre dans les 6 essais, il a gagné, sinon il a perdu.
for i in range (6):
    nombre_sring=input("entrer un nombre entre 0 et 100: ")
    nbr=int(nombre_sring)
    if nbr<variable_aleatoire:
        print("trop petit")
    elif nbr>variable_aleatoire:
        print("trop grand")
    else:
        print ("nombre a deviner")


#P4 Calcul de l'indice de masse corporelle

#Q1 IMC = Poids (kg) / Taille² (m) 
#Q2 Mon IMC= 64/1.64
IMC= 64/(1.65)**2
print (IMC)
#Q3 Implémenter la formule dans une fonction
# a=poids en kg et b=taille en m

def fonction_IMC (a,b): 
    IMC= a/(b)**2
    return IMC
print(fonction_IMC(71,1.7))
#Q4 Demander les informations nécessaire à l’utilisateur avec la fonction input().
x= input(" poids(kg)= ??? ")
y= input (" taille (m)= ??? ")
p=float(x)
t=float(y)
print(fonction_IMC(p,t))
imc= fonction_IMC(p,t)
#5 Avertir l’utilisateur en cas d’IMC trop bas ou trop haut.
if imc <18.5:
    print("Trop bas")
if imc>=18.5 and imc<25:
    print("normal")
else:
    print("trop haut")

#P5 loucherbem

#Q1 loucherbem= boucher
#Q2 Tester si un mot commence par une consonne. Si ce n’est pas le cas, on ne fera rien. et #Q3.
""" Q3 Si c’est le cas, déplacer la première lettre (qui est une consonne) à la fin du mot, remplacer cette première lettre par ‘l’ 
et rajouter ‘em’ à la fin. Par exemple : “boucher” -> “oucherb” -> “loucherb” -> “loucherbem”."""

consonne = [ 'B', 'C', 'D', 'F', 'G', 'H',  'J', 'K', 'L', 'M', 'N',  'P', 'Q', 'R', 'S', 'T','V', 'W', 'X', 'Z']
mot1= "EOLIENNE"
mot2="Boucher"
def fonction_loucherbem(mot):
    if mot[0] in consonne:
        p=mot[0] #premiere lettre
        r=mot[1:] #reste
        return("l"+r+p+"em")
    else:
        return ("")
print(fonction_loucherbem(mot1))
print(fonction_loucherbem(mot2))
#Q4 Appliquer cette transformation à tous les mots d’une phrase.
#Q5 Utiliser la fonction input() pour demander une phrase à l’utilisateur avant de la transformer.
def fonctin_phrase(phrase): 
    liste_phrase= phrase.split(" ")
    cdc_sortie=""
    for chaque_mot in liste_phrase:
      temp= fonction_loucherbem(chaque_mot)
      cdc_sortie= cdc_sortie+temp+" "
    return cdc_sortie
ph=input("entrez une phrase(attention commencez chaque mot par une majuscule): ")
print(fonctin_phrase(ph))
#Q6 Implémenter la transformation inverse.
mot1= "loucherbem"
mot2="lreethipem"
def fonction_reverseloucherbem(mot):
    reste=mot[1:-3]
    premier=mot[-3]
    return premier+reste
print(fonction_reverseloucherbem(mot1))
print(fonction_reverseloucherbem(mot2))
















