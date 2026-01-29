# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

# TODO: Lire n (int) et statut (str)

# TODO: Validation (n >= 0 et statut dans {O, N})

# TODO: Chercher la meilleure combinaison (A, B, C, D)

# TODO: Calculer et afficher le resultat exact (6 lignes)
try:
    n = int(input("Entrez le nombre de billets necessaires : "))
    etudiant = input("Entrez le statut etudiant (O/N) : ")
except ValueError:
    print("Erreur - donnees invalides.")
    exit()

if n <= 0 or (etudiant != "O" and etudiant != "N"):
    print("Erreur - donnees invalides.")
    exit()

A = 0
B = 0
C = 0
D = 0
T = n

while n != 0:
    if n >= 24:
        A += 1
        n -= 24
        continue
    elif n >= 12:
        B += 1
        n -= 12
        continue
    elif n >= 5:
        C += 1
        n -= 5
        continue
    else:
        D += n
        n -= n

if etudiant == "O":
    rabais = 0.88
else:
    rabais = 1

prix_T = rabais * (A * 66.00 + B * 36.00 + C * 15.75) + D * 3.60

print(f"Forfaits de 24 billets - {A}")
print(f"Forfaits de 12 billets - {B}")
print(f"Forfaits de 5 billets - {C}")
print(f"Billets unitaires - {D}")
print(f"Total billets - {T}")
print(f"Prix total - {prix_T:06.2f}$")