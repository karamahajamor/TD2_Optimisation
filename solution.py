import math
import random


# EXERCICE 2 : PROBLEME DE TRANSPORT

demandes = [4, 5, 8]
couts = [
    [5, 3, 4],
    [6, 7, 2]
]
def cout_transport(d1):
    d2 = [demandes[i] - d1[i] for i in range(3)]
    total = 0
    for i in range(3):
        total += couts[0][i] * d1[i]
        total += couts[1][i] * d2[i]
    return total


def voisins_transport(solution):
    voisins = []
    for depart in range(3):
        for arrivee in range(3):
            if depart != arrivee:
                if solution[depart] > 0:
                    if solution[arrivee] < demandes[arrivee]:
                        voisin = solution.copy()
                        voisin[depart] -= 1
                        voisin[arrivee] += 1
                        voisins.append(voisin)
    return voisins


def recherche_taboue_transport():
    solution = [4, 0, 4]  
    meilleure = solution.copy()
    liste_taboue = []
    duree_taboue = 3
    for iteration in range(100):
        candidats = voisins_transport(solution)
        candidats_valides = []
        for candidat in candidats:
            est_tabou = tuple(candidat) in liste_taboue
            aspiration = cout_transport(candidat) < cout_transport(meilleure)
            if not est_tabou or aspiration:
                candidats_valides.append(candidat)
        if not candidats_valides:
            break
        solution = min(candidats_valides, key=cout_transport)
        liste_taboue.append(tuple(solution))
        if len(liste_taboue) > duree_taboue:
            liste_taboue.pop(0)
        if cout_transport(solution) < cout_transport(meilleure):
            meilleure = solution.copy()
    return meilleure


meilleure_d1 = recherche_taboue_transport()
meilleure_d2 = [
    demandes[i] - meilleure_d1[i]
    for i in range(3)
]

print("EXERCICE 2 - RECHERCHE TABOUE")
print("D1 livre à M1, M2, M3 :", meilleure_d1)
print("D2 livre à M1, M2, M3 :", meilleure_d2)
print("Coût total :", cout_transport(meilleure_d1))


# EXERCICE 3 : VOYAGEUR DE COMMERCE


distances = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17,
    (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13
}

tour_initial = [1, 2, 3, 4, 5, 6, 7, 8]


def cout_tour(tour):
    total = 0
    for i in range(len(tour)):
        ville1 = tour[i]
        ville2 = tour[(i + 1) % len(tour)]
        arete = tuple(sorted((ville1, ville2)))
        if arete not in distances:
            return None
        total += distances[arete]
    return total


def voisins_tour(tour):
    voisins = []
    for i in range(1, len(tour) - 1):
        for j in range(i + 1, len(tour)):
            voisin = tour.copy()
            voisin[i], voisin[j] = voisin[j], voisin[i]
            if cout_tour(voisin) is not None:
                voisins.append(voisin)
    return sorted(voisins)


def recuit_simule():
    solution = tour_initial.copy()
    meilleure = solution.copy()

    temperature = 10
    alpha = 0.8
    hasard = random.Random(73)
    for iteration in range(5):
        candidats = voisins_tour(solution)
        if not candidats:
            break
        voisin = hasard.choice(candidats)
        variation = cout_tour(voisin) - cout_tour(solution)
        if variation <= 0:
            solution = voisin
        elif hasard.random() < math.exp(-variation / temperature):
            solution = voisin
        if cout_tour(solution) < cout_tour(meilleure):
            meilleure = solution.copy()
        temperature = alpha * temperature
    return meilleure


def recherche_taboue_tour():
    solution = tour_initial.copy()
    meilleure = solution.copy()
    liste_taboue = []
    duree_taboue = 7
    for iteration in range(100):
        candidats = voisins_tour(solution)
        candidats_valides = []
        for candidat in candidats:
            est_tabou = tuple(candidat) in liste_taboue
            aspiration = cout_tour(candidat) < cout_tour(meilleure)
            if not est_tabou or aspiration:
                candidats_valides.append(candidat)
        if not candidats_valides:
            break
        solution = min(candidats_valides, key=cout_tour)
        liste_taboue.append(tuple(solution))
        if len(liste_taboue) > duree_taboue:
            liste_taboue.pop(0)
        if cout_tour(solution) < cout_tour(meilleure):
            meilleure = solution.copy()
    return meilleure


def afficher_tour(nom, tour):
    circuit = tour + [tour[0]]
    print(nom, ":", "-".join(map(str, circuit)))
    print("Coût :", cout_tour(tour))
print()
print("EXERCICE 3 - RECUIT SIMULÉ")
afficher_tour("Meilleur circuit", recuit_simule())
print()
print("EXERCICE 3 - RECHERCHE TABOUE")
afficher_tour("Meilleur circuit", recherche_taboue_tour())