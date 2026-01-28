# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]

# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter

# TODO: Calculer les intensites brutes (liste de 8 floats)

# TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])

# TODO: Afficher la grille (10 lignes) puis la ligne des labels\

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))
D = int(input("D:"))
E = int(input("E:"))
F = int(input("F:"))
G = int(input("G:"))
H = int(input("H:"))
liste_place = [A, B, C, D, E, F, G, H]

if A < 0 or B < 0 or C < 0 or D < 0 or E < 0 or F < 0 or G < 0 or H < 0:
    print("Erreur - donnees invalides.")
    exit()
liste_intensite_brute =[]
for i in range(len(FACTEURS)):
    liste_intensite_brute.append(liste_place[i] * FACTEURS[i] )

niveau = []
intensite_max = max(liste_intensite_brute)


for i in range(len(liste_intensite_brute)):
    niveau.append(int((liste_intensite_brute[i] / intensite_max) * 10 + 0.5))

hauteur_niveau = ["10 |", " 9 |", " 8 |", " 7 |", " 6 |", " 5 |", " 4 |", " 3 |"," 2 |"," 1 |"]

indice_hauteur_niveau = 10
liste_str_lettre = ["A", "B","C","D","E","F","G","H"]

for i in range (10):
    print(hauteur_niveau[i], end=" ")


    for y in range(len(niveau)):
        if niveau[y] >= indice_hauteur_niveau:
            print("❚",end=" ")
        else:
            print(".",end=" ")
        
    print()
    indice_hauteur_niveau -= 1

for i in range(len(liste_str_lettre) + 2):
    if i > 1:
        print(liste_str_lettre[i - 2],end=" ") 
    else:
        print(" ",end=" ")






