# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)

# TODO: Lire les 4 valeurs (int)

# TODO: Valider les donnees (matchs >= 0, durees > 0)

# TODO: Calculer les minutes totales (football, soccer, total)

# TODO: Convertir en heures/minutes et afficher exactement 4 lignes
try:
    nom = input("Entrez votre nom complet : ")
    match_football = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
    duree_football = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
    match_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
    duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
except ValueError:
    print("Erreur - donnees invalides.")
    
if match_football <= 0 or duree_football < 0 or match_soccer <= 0 or duree_soccer < 0:
    print("Erreur - donnees invalides.")
    exit()
    
total_min_football = match_football * duree_football
total_min_soccer = match_soccer * duree_soccer

heure_football = total_min_football // 60
min_restant_football =  total_min_football % 60
heure_soccer = total_min_soccer // 60
min_restant_soccer = total_min_soccer % 60

heure_total = heure_football + heure_soccer + ((min_restant_football + min_restant_soccer) % 60)
min_total = (min_restant_football + min_restant_soccer) % 60

print(f"Bonjour {nom}")
print(f"Football (carabin): {match_football} match(s), {heure_football}h{min_restant_football:02d} de visionnage")
print(f"Soccer (carabins): {match_soccer} match(s), {heure_soccer}h{min_restant_soccer:02d} de visionnage")
print(f"Total: {heure_total}h{min_total:02d}")


