#!/usr/bin/env python3

import random
import common  # N'utilisez pas la syntaxe "from common import XXX"
import itertools

possibles = None
dernier_coup = None


def init():
    global possibles, dernier_coup
    possibles = set(''.join(p) for p in itertools.product(common.COLORS, repeat=common.LENGTH))
    dernier_coup = None


def codebreaker(evaluation_p):
    global possibles, dernier_coup

    if evaluation_p is not None and dernier_coup is not None:
        common.maj_possibles(possibles, dernier_coup, evaluation_p)

        # Sécurité / debug : si l'ensemble devient vide, il y a incohérence
        if len(possibles) == 0:
            raise RuntimeError(
                "Ensemble des possibles vide : incohérence détectée.\n"
                "Ca vient presque toujours de common.evaluation (ou de l'ordre des arguments).\n"
                f"Dernier coup = {dernier_coup}, evaluation reçue = {evaluation_p}"
            )

    dernier_coup = random.choice(tuple(possibles))
    return dernier_coup
