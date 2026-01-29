# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math

# TODO: Lire les 4 valeurs

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)

# TODO: Afficher la phrase exacte

import math
try:
    distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
    attente_navette = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
    temps_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
    controle = float(input("Entrez le temps de controle a l'entree (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
    exit()

if distance <= 0 or attente_navette <= 0 or temps_metro <= 0 or controle < 0:
    print("Erreur - donnees invalides.")
    exit()
marche  = math.ceil((distance * 60 / 5 + controle) + 0.5)
navette = math.ceil((attente_navette + distance * 60 / 18 + controle) + 0.5)
metro   = math.ceil((temps_metro + controle) + 0.5)

if marche == navette == metro:
    print("Egalite : marcher, navette et metro.")
    exit()
liste_transport = [["marche",marche], ["navette", navette], ["metro", metro]]
plus_petit = 0
indice_petit = 0

for i in range(3):  
    if plus_petit > liste_transport[i][1]:
        plus_petit = liste_transport[i][1]
        indice_petit = i

        
for i in range(3):

    if liste_transport[i][1] == plus_petit and liste_transport[indice_petit][0] != liste_transport[i][0]:
        if indice_petit + i == 1:
            print("Egalite : marche et navette.")
            exit()

        elif indice_petit + i == 2:
            print("Egalite : marche et metro.")
            exit()

        elif indice_petit + i == 3:
                print("Egalite : navette et metro.")
                exit()
print(f"Option la plus rapide : {liste_transport[indice_petit][0]}.")
