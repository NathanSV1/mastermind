#!/usr/bin/env python3
import itertools

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(proposition, solution):

    # normalisation
    if isinstance(proposition, list):
        proposition = proposition[0]
    if isinstance(solution, list):
        solution = solution[0]

    # initialisation
    bien_places = 0
    mal_places = 0

    # transformation en listes pour pouvoir marquer les éléments utilisés
    prop = list(proposition)
    sol = list(solution)

    # comptage des bien placés
    for i in range(LENGTH):
        if prop[i] == sol[i]:
            bien_places += 1
            prop[i] = None
            sol[i] = None

    # comptage des mal placés
    for i in range(LENGTH):
        if prop[i] is not None and prop[i] in sol:
            mal_places += 1
            j = sol.index(prop[i])
            sol[j] = None

    return (bien_places, mal_places)

def donner_possibles(combinaison, evaluation_associee):
    """
    Renvoie l'ensemble des combinaisons possibles après un essai donné et une évaluation donnée en arguments
    """
    # normalisation (important)
    if isinstance(combinaison, list):
        combinaison = combinaison[0]

    bp, mp = evaluation_associee

    possibles = set() # set des combinaisons encore possibles pour le codebreaker

    for p in itertools.product(COLORS, repeat=LENGTH): # pour p dans le produit cartésien de COLORS * LENGHT
        candidate = ''.join(p)
        if evaluation(combinaison, candidate) == (bp, mp):
            possibles.add(candidate)

    return possibles

def maj_possibles(possibles : set, combinaison, evaluation_associee) -> None:
    """
    Met à jour l'ensemble le set des combinaisons possibles en place (ne retourne rien)
    """
    # normalisation
    if isinstance(combinaison, list):
        combinaison = combinaison[0]

    bp, mp = evaluation_associee

    a_supprimer = set()

    for c in possibles:
        if evaluation(combinaison, c) != (bp, mp):
            a_supprimer.add(c)

    possibles.difference_update(a_supprimer) # A.difference_update(B) : Remove all elements of B from A 
