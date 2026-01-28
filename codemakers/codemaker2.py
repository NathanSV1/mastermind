#!/usr/bin/env python3

import common  
import itertools

possibles = None # Avant on fixait une solution à l'avance, maintenant on 
                 # la fait "glisser" au fur et à mesure que l'on avance ! 


def init():
    global possibles
    possibles = set(''.join(p) for p in itertools.product(common.COLORS, repeat=common.LENGTH))

def codemaker(combinaison):
    """ Ici on introduit le droit pour le codemaker de changer de solution en cours de jeu, tant que celle-ci
        reste compatible avec les précédentes évaluations. Un tel tricheur serait donc en théorie indétectable !

        À chaque combinaison que proposera le codebreaker on :
            - donne l'évaluation qui laisse le plus de possibilités (i.e qui ralentit codebreaker)
            - on met à jour les possibles restants

        Formellement, à chaque proposition g:
            - on partitionne possibles en paquets selon evaluation(g, possible)
            - on choisit le paquet le plus gros
            - on met possibles = ce paquet
            - on renvoit l'évaluation choisie
    """

    global possibles

    if isinstance(combinaison, list):
        combinaison = combinaison[0]

    # partition par évaluation
    buckets = {}
    for s in possibles:
        ev = common.evaluation(combinaison, s)  # proposition, solution_candidate
        buckets.setdefault(ev, set()).add(s) # pour la clé ev dans le dict buckets : si le set existe on y ajoute s, sinon on en créé un vide et on y ajoute s

    # choisir l'évaluation qui garde le plus de possibilités (en évitant "gagné" si possible)
    best_ev = None # initialisation
    best_size = -1

    for ev, sols in buckets.items():
        if ev[0] == common.LENGTH:
            continue
        if len(sols) > best_size:
            best_size = len(sols)
            best_ev = ev

    if best_ev is None:
        best_ev = (common.LENGTH, 0)

    possibles = buckets[best_ev]
    return best_ev
