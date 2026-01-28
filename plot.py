#!/usr/bin/env python3

# ----- PLOTS DONE WITH AI -----

import matplotlib.pyplot as plt
import play
import random
import common

# Importez ici votre codebreaker 
from codebreakers import codebreaker2
from codebreakers import codebreaker3

# et votre codemaker
from codemakers import codemaker1
from codemakers import codemaker2

def launch(N_PARTIES: int = 1000, codebreaker = codebreaker2, codemaker = codemaker1) -> list:
    resultats = []

    # Lancer N_PARTIES parties
    for i in range(N_PARTIES):
        essais = play.play(codemaker, codebreaker, quiet=True)
        resultats.append(essais)

    return resultats

def plot1(resultats, N_PARTIES = 1000):
    # Calcul de la moyenne expérimentale
    moyenne = sum(resultats) / len(resultats)
    print(f"Nombre moyen d'essais : {moyenne:.2f}")
    print(f"Maximum : {max(resultats)}, Minimum : {min(resultats)}")


    # Histogramme
    plt.hist(resultats, bins=50, color='skyblue', edgecolor='black')
    plt.title(f"Histogramme du nombre d'essais du codebreaker2 ({N_PARTIES} parties)")
    plt.xlabel("Nombre d'essais")
    plt.ylabel("Nombre de parties")

    # Tracer la moyenne expérimentale en rouge
    plt.axvline(x=moyenne, color='red', linestyle='--', linewidth=1, label=f"Moyenne ≈ {moyenne:.2f}")

    plt.legend()
    plt.show()

def plot_codemaker_1_VS_2_CB2(N_PARTIES = 1000):
    r1, r2 = [], []

    for _ in range(N_PARTIES):
        r1.append(play.play(codemaker1, codebreaker2, quiet=True))
        r2.append(play.play(codemaker2, codebreaker2, quiet=True))

    m1 = sum(r1)/len(r1)
    m2 = sum(r2)/len(r2)

    gain_abs = m2 - m1
    gain_pct = (gain_abs / m1) * 100 if m1 != 0 else 0.0

    print(f"codemaker1 (honnête) vs codebreaker2 : moyenne = {m1:.2f}")
    print(f"codemaker2 (tricheur) vs codebreaker2 : moyenne = {m2:.2f}")
    print(f"Gain du tricheur : +{gain_abs:.2f} coups ({gain_pct:+.1f}%)")

    fig, ax = plt.subplots(figsize=(10, 4.8))

    bp = ax.boxplot(
        [r1, r2],
        vert=False,
        labels=["honnête", "tricheur"],
        showmeans=True,
        patch_artist=True,   # <-- permet de colorer
        widths=0.55
    )

    # --- Couleurs "pro" ---
    colors = ["#4C78A8", "#F58518"]  # bleu / orange
    for patch, c in zip(bp["boxes"], colors):
        patch.set_facecolor(c)
        patch.set_alpha(0.30)
        patch.set_edgecolor(c)
        patch.set_linewidth(2)

    # moustaches / caps
    for w in bp["whiskers"]:
        w.set_linewidth(1.6)
    for c in bp["caps"]:
        c.set_linewidth(1.6)

    # médianes (noir)
    for med in bp["medians"]:
        med.set_color("#222222")
        med.set_linewidth(2.4)

    # moyennes (rouge)
    for mean in bp["means"]:
        mean.set_color("#D62728")
        mean.set_linewidth(2.4)

    # --- Petit nuage de points (jitter) pour rendre la distribution plus "vivante" ---
    # (facultatif, mais ça rend vraiment bien)
    def jitter_scatter(values, y_center, color):
        ys = [y_center + (random.random() - 0.5) * 0.18 for _ in values]
        ax.scatter(values, ys, s=12, alpha=0.18, color=color, edgecolors="none")

    jitter_scatter(r1, 1, colors[0])
    jitter_scatter(r2, 2, colors[1])

    # lignes verticales sur les moyennes (en plus du symbole mean)
    ax.axvline(m1, color=colors[0], linestyle="--", linewidth=1.2, alpha=0.9)
    ax.axvline(m2, color=colors[1], linestyle="--", linewidth=1.2, alpha=0.9)

    # --- Annotation gain ---
    x_max = max(max(r1), max(r2))
    ax.text(
        x_max * 0.98, 2.55,
        f"Gain du tricheur : +{gain_abs:.2f} coups ({gain_pct:+.1f}%)\n"
        f"Moyennes : honnête {m1:.2f} | tricheur {m2:.2f}",
        ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#999999", alpha=0.95)
    )

    ax.set_xlabel("Nombre d'essais")
    ax.set_title(f"Comparaison : codemaker honnête vs tricheur ({N_PARTIES} parties)")
    ax.grid(True, axis="x", alpha=0.25)

    plt.tight_layout()
    plt.show()

def plot_codemaker_1_VS_2_CB3(N_PARTIES = 30):
    r1, r2 = [], []

    for _ in range(N_PARTIES):
        r1.append(play.play(codemaker1, codebreaker3, quiet=True))
        r2.append(play.play(codemaker2, codebreaker3, quiet=True))

    m1 = sum(r1)/len(r1)
    m2 = sum(r2)/len(r2)

    gain_abs = m2 - m1
    gain_pct = (gain_abs / m1) * 100 if m1 != 0 else 0.0

    print(f"codemaker1 (honnête) vs codebreaker3 : moyenne = {m1:.2f}")
    print(f"codemaker2 (tricheur) vs codebreaker3 : moyenne = {m2:.2f}")
    print(f"Gain du tricheur : +{gain_abs:.2f} coups ({gain_pct:+.1f}%)")

    fig, ax = plt.subplots(figsize=(10, 4.2))

    # --- Nuage de points aligné ---
    y1 = [1 + (random.random() - 0.5) * 0.06 for _ in r1]
    y2 = [2 + (random.random() - 0.5) * 0.06 for _ in r2]

    ax.scatter(r1, y1, s=18, alpha=0.5, color="#4C78A8", label="honnête")
    ax.scatter(r2, y2, s=18, alpha=0.5, color="#F58518", label="tricheur")

    # --- Mise en forme ---
    ax.set_yticks([1, 2])
    ax.set_yticklabels(["codemaker honnête", "codemaker tricheur"])
    ax.set_xlabel("Nombre d'essais avant victoire")
    ax.set_title(f"Codebreaker3 (minimax) ({N_PARTIES} parties)")

    ax.grid(True, axis="x", alpha=0.25)
    ax.legend(loc="lower right")

    # --- Annotation interprétative ---
    x_max = max(max(r1), max(r2))
    ax.text(
        x_max * 0.98, 2.25,
        f"Moyennes : honnête {m1:.2f} | tricheur {m2:.2f}\n"
        f"Gain du tricheur : +{gain_abs:.2f} coups ({gain_pct:+.1f}%)",
        ha="right", va="top",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#999999", alpha=0.95)
    )

    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    n = 1000

    # Lancer n parties :
    res = launch(n, codebreaker2, codemaker1)
    
    # plot le resultat :
    plot1(res, n)

    #plot_codemaker_1_VS_2()
    #plot_codemaker_1_VS_2_CB3()



