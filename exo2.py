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
try:
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    F = int(input())
    G = int(input())
    H = int(input())
    
    liste_place = [A, B, C, D, E, F, G, H]

    if A < 0 or B < 0 or C < 0 or D < 0 or E < 0 or F < 0 or G < 0 or H < 0:
        print("Erreur - donnees invalides.")
        exit()
    liste_intensite_brute =[]
    for i in range(len(FACTEURS)):
        liste_intensite_brute.append(liste_place[i] * FACTEURS[i] )

    niveau = []
    intensite_max = max(liste_intensite_brute)

    if intensite_max != 0:

        for i in range(len(liste_intensite_brute)):
            niveau.append(int((liste_intensite_brute[i] / intensite_max) * 10 + 0.5))
    else:
        for i in range(8):
            niveau.append(0) 


    liste_str_lettre = "     A B C D E F G H"

    for i in range(10, 0, -1):
        S = ""
        for y in range(8):
            if niveau[y] >= i:
                S += "❚ "
            else:
                S += ". "

        print(f"{i:2} | {S.strip()}")
    print(liste_str_lettre)
except ValueError:
    print("Erreur - donnees invalides.")





