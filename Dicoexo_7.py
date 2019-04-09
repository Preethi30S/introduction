# Exercices sur les dictionnaires

#Recopier les exemples du cours et vérifier qu’ils fonctionnent.

#exemple 1
dico_couleur= {"vert": "Couleur d’un arbre" , "rouge" : "Couleur d’un rubis", "bleu" : "Couleur du ciel"}
print(dico_couleur["vert"])
print(len(dico_couleur))

#exemple 2
dico_routine={
8: "Lever" ,
9 : "Cours de botanique",
12 : "Déjeuner",
14 : "Cours de programmation", 
18 : "RDV chez le dentiste"
}
print(dico_routine[8])
print(len(dico_routine))

#exemple 3
dico_nom={"nom": "Poirot" , "prénom": "Hercule", "profession": "détective", "nationalité": "Belge", "age" : 45,}
job=dico_nom["profession"]
print(job)
dico_nom["sexe"]="garçon" #pour rajouter un couple (clé,valeur) dans le dictionnaire
dico_nom["nom"]="Etienne" #pour remplacer un couple (clé,valeur) dans le dictionnaire
print(dico_nom)


"""Définir un dictionnaire qui contient la valeur 150 pour la clé “soda”, la valeur 50 pour la clé “pâtes” et 
la valeur 2 pour la clé “champignons”."""
dico_food={"soda":150,"pâtes":50,"champignons":2}

"""Définir une fonction qui renvoie le nombre de jours d’un mois. Par exemple : nb_jours("Mars") renvoie 31. 
On suppose que l’année en cours n’est pas bisextile."""

def fmois(CdC):
    dico_mois={"Janv":31,"Feb":28,"Mars":31,"Avril":30,"Mai":31,"Juin":30,"Juillet":31,"Aout":31,"Sept":30,"Oct":31,"Dec":31}
    return dico_mois[CdC]
print(fmois("Janv"))

#Même exercice que précédemment, mais on prend en compte les années bisextiles.
def fleapyear (Y):
    if Y % 4==0 and Y % 100 != 0:
        return(True)
    elif Y % 400 == 0:
        return(True)
    else:
        return(False)

def fanneemois(y,CdC):
    dico_mois={"Janv":31,"Feb":28,"Mars":31,"Avril":30,"Mai":31,"Juin":30,"Juillet":31,"Aout":31,"Sept":30,"Oct":31,"Dec":31}
    bisex_ou_non= fleapyear(y)
    if bisex_ou_non==True:
        dico_mois["Feb"]=29
        return dico_mois[CdC]
    else:
        return dico_mois[CdC]
print(fanneemois(2020,"Feb"))

