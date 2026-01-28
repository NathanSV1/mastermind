#!/usr/bin/env python3

import sys
import random
import common 

# variable globale pour la solution
solution = None


def init():
    """
    Initialisation du codemaker : on choisit la combinaison secrète
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def codemaker(combinaison):
    """
    Évalue la combinaison proposée par le codebreaker
    Renvoie (nombre de plots bien placés, nombre de plots mal placés)
    """
    global solution
    # on appelle la fonction d'évaluation de common.py
    return common.evaluation(combinaison, solution)
