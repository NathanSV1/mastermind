#!/usr/bin/env python3

import random
import itertools
import common 

# Tous les coups possibles (univers)
ALL = None

# Ensemble des solutions encore possibles
possibles = None

# Dernier coup joué (pour pouvoir mettre à jour avec l'évaluation reçue)
dernier_coup = None

# Mettre True pour considérer tous les coups (plus optimal, plus lent)
# Mettre False pour ne tester que les coups encore possibles (plus rapide, moins optimal).
USE_ALL_GUESSES = True


def init():
    global ALL, possibles, dernier_coup
    ALL = [''.join(p) for p in itertools.product(common.COLORS, repeat=common.LENGTH)]
    possibles = set(ALL)
    dernier_coup = None


def _score_pire_cas(guess, sols_possibles):
    """
    Renvoie la taille du plus gros 'bucket' obtenu en jouant guess,
    i.e. max_{evaluation} |{s in sols_possibles : evaluation(guess,s)=evaluation}|

    On regarde comment un guess partitionne possibles en buckets et on prends le guess qui fait le plus gros bucket
    """
    counts = {}
    for s in sols_possibles:
        ev = common.evaluation(guess, s)  # proposition, solution
        counts[ev] = counts.get(ev, 0) + 1
    return max(counts.values()) if counts else 0


def codebreaker(evaluation_p):
    global possibles, dernier_coup, ALL

    # 1) Mise à jour des possibles avec l'évaluation du dernier coup dans le cas ou on n'est pas au premier coup
    if evaluation_p is not None and dernier_coup is not None:
        common.maj_possibles(possibles, dernier_coup, evaluation_p)

    # 2) Si une seule solution possible, on la joue
    if len(possibles) == 1:
        dernier_coup = next(iter(possibles))
        return dernier_coup

    # 3) Choix minimax (pire cas)
    candidats = ALL if USE_ALL_GUESSES else list(possibles)

    best_guess = None
    best_worst = None

    # Petite optimisation : si on est déjà très bas, inutile de chercher trop loin
    # (facultatif)
    sols_list = list(possibles)

    for g in candidats:
        worst = _score_pire_cas(g, sols_list)

        if (best_worst is None) or (worst < best_worst):
            best_worst = worst
            best_guess = g
        elif worst == best_worst:
            # tie-break : on préfère un guess qui est lui-même possible
            if (best_guess not in possibles) and (g in possibles):
                best_guess = g

        # si pire cas = 1, c'est parfait (on force la solution au coup suivant)
        if best_worst == 1 and best_guess in possibles:
            break

    dernier_coup = best_guess if best_guess is not None else random.choice(sols_list) # si on a jamais joué alors on renvoi un random
    return dernier_coup
