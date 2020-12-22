"""
ALGORYTMY GENETYCZNE

TODO:   ładnie zakomentować kod
TODO:   zmienić nazwy zmiennych na czytelniejsze
"""

import numpy as np
import random
import matplotlib.pyplot as plt


def f_x(_w, _v, _p, _C):
    """
    Funkcja przystosowania
    :param _w: tablica wag
    :param _v: tablica wartości
    :param _p: tablica populacji np [0, 1, 1, 0 ... ]
    :param _C: maksymalne obciazenie plecaka
    :return: tablica przystosowania
    """
    population_fitness = []
    for i in range(len(_p)):
        individual_fitness = np.sum(_p[i] * _v)
        individual_weight = np.sum(_p[i] * _w)
        if individual_weight > _C:
            population_fitness.append(0)
        else:
            population_fitness.append(individual_fitness)

    return population_fitness


def sort_by_fitness(arr):
    return arr[1]


def generate_new_population(current_population):
    # mutacja
    mutants = []
    for individual in current_population:
        new_individual = []
        for x in individual:
            if random.random() < epsilon:
                new_individual.append(int(not x))
            else:
                new_individual.append(x)
        mutants.append(new_individual)

    mutants = np.array(mutants)

    total = np.concatenate((current_population, mutants))
    total_fitness = f_x(w, v, total, C)

    zipped = zip(total, total_fitness)
    zipped_sorted = sorted(zipped, key=sort_by_fitness, reverse=True)
    bests = zipped_sorted[:len(zipped_sorted) // 2]
    new_p = [x[0] for x in bests]
    new_p = np.array(new_p)

    best_in_p = new_p[0]
    v_best_in_p = np.sum(best_in_p * v)
    w_best = np.sum(best_in_p * w)
    if w_best > C:
        v_best_in_p = 0
    best_story.append(v_best_in_p)

    return new_p


N = 100  # liczba artykułów
individuals_in_population = 100  # osobnikow w populacji
epsilon = 0.15  # wspolczynnik do mutacji
iterations = 100  # inaczej liczba generacji


w = np.random.randint(1, 10, N)  # waga
v = np.random.randint(0, 30, N)  # wartosc
C = N*2  # maksymalna pojemnosc plecaka
best_story = []
print(f"wagi: {w}")
print(f"wartosc: {v}")

initialPopulation = np.random.randint(0, 2, (individuals_in_population, N))
curr_pop = initialPopulation
for i in range(iterations):
    new_population = generate_new_population(curr_pop)
    curr_pop = new_population


best = curr_pop[0]
print(f"najlepszy: {best}")
print(f"wartosc {np.sum(best * v)}")
print(f"waga {np.sum(best * w)}")

plt.plot(best_story)
plt.title(f"Przystosowanie najlepszego osobnika w populacji dla N={N}")
plt.ylabel("Przystosowanie")
plt.xlabel(f"Liczba iteracji\npojemność plecaka={C}, liczba iteracji={iterations}, osobników w populacji={individuals_in_population}")
# plt.figtext(0.5, 0.01, "one text and next text", ha="center", fontsize=6)
plt.show()





