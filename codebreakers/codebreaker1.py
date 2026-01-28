#!/usr/bin/env python3

import random
import common
import itertools

# variables globales au module
possibles = None
index = 0


def init():
    """
    Initialisation : on génère toutes les combinaisons possibles
    et on les mélange
    """
    global possibles, index
    possibles = [''.join(p) for p in itertools.product(common.COLORS, repeat=common.LENGTH)]
    random.shuffle(possibles) # optionnel
    index = 0


def codebreaker(evaluation_p):
    """
    Version 1 du codebreaker : joue aléatoirement sans jamais répéter une combinaison.
    (L'évaluation n'est pas encore utilisée)
    """
    global possibles, index
    combinaison = possibles[index]
    index += 1
    return combinaison
