"""
ALGORYTMY GENETYCZNE - ZADANIE PCHANIA WÓZKA

Marek		Mikulski	165745
Maciej	    Kuraż		165737
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import random


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#############################################################
#                 Funkcja przystosowania                    #
# Dla każdego osobnika całej populacji (70 osobników        #
# rodzicielskich oraz 70 osobników potomnych (zmutowanych)) #
# obliczamy funkcję przystosowania wartość współczynnika J  #
# po ówczesnym odkodowaniu                                  #
#############################################################
def fitness_function(_N, population):
    all_fitness = []
    u = []
    arr = []

    for man in population:
        sum_u = 0
        x2 = 0
        x1 = 0
        a = 0
        b = 20

        arr.clear()
        u.clear()
        man = man * values

        ###########################################
        # Odkodowanie chromosomu osobnika, w celu #
        # uzyskania zawartych w nim sterowań (u)  #
        ###########################################
        for j in range(N):
            arr.append(man[a:b])
            a = a + 20
            b = b + 20
            u.append(np.sum(arr[j]))

        #########################################################
        # Obliczenie kolejnych stanów na bazie modelu stanowego #
        #########################################################
        for k in range(0, _N):
            x1_new = x2
            x2_new = 2 * x2 - x1 + 1 / (N ** 2) * u[k]
            sum_u = sum_u + (u[k] ** 2)
            x1 = x1_new
            x2 = x2_new

        ###########################################
        # Obliczenie wskaźnika jakości sterowania #
        ###########################################
        J = x1 - sum_u / (2 * _N)
        all_fitness.append(J)

    best_fitness_individuals.append(max(all_fitness))
    return all_fitness


####################################################################
# Funkcja pozwalająca na wybór opcji sortowania w funkcji sorted() #
####################################################################
def fitness_sort(array):
    return array[1]


####################################################################################
# Tworzenie nowej populacji poprzez mutacje oraz selekcje polegająca na odrzuceniu #
# gorszej połowy osobników na podstawie wartości ich funkcji przystosowania        #
####################################################################################
def make_new_population(_current_population):
    #################################################################
    # Mutacja osobników z prawdopodobieństwem równym epsilon = 20%  #
    # polegająca na zamianie wartości bitów na przeciwne            #
    #################################################################
    mutated_population = []
    mutated_population.clear()
    for man in _current_population:
        new_man = []
        for bit in man:
            z = random.random()
            if z < epsilon:
                new_man.append(int(not bit))
            else:
                new_man.append(bit)
        mutated_population.append(new_man)

    mutated_population = np.array(mutated_population)

    whole_population = np.concatenate((_current_population, mutated_population))

    fitness_array = fitness_function(N, whole_population)

    ##########################################################################
    # Sortujemy od najlepszych osobników, aby następnie usunąć gorszą połowę #
    ##########################################################################
    combined = zip(whole_population, fitness_array)
    population_sorted = sorted(combined, key=fitness_sort, reverse=True)
    better_half = population_sorted[:len(population_sorted) // 2]
    # Wyciągnięcie samej populacji z krotki zawierającej osobnika i jego wartość J
    new_p = [x[0] for x in better_half]
    new_p = np.array(new_p)
    return new_p


############################################
# Ustawienie wartości parametrów symulacji #
############################################
our_solution = 0
size_of_population = 70
epsilon = 0.20
iterations = 6234
N = 5

values = []
best_fitness_individuals = []

#################################################
# Wygenerowanie tablicy wartości do dekodowania #
#################################################
for i in range(0, 20 * N):
    x = random.uniform(0, 0.1)
    values.append(x)

###########################################################
# Stworzenie populacji początkowej o określonej wielkości #
###########################################################
starting_population = np.random.randint(0, 2, (size_of_population, 20 * N))
current_population = starting_population

start_all_t = time.time()

##################################################
# Pętla wykonująca algorytm określoną ilość razy #
##################################################
for i in range(iterations):
    start_t = time.time()
    new_population = make_new_population(current_population)
    duration = time.time() - start_t
    our_solution = max(best_fitness_individuals)
    current_population = new_population
    print(f"{BColors.WARNING}########################################{BColors.ENDC}")
    print(f"{BColors.WARNING}########### ITERATIONS ", i, f"###########{BColors.ENDC}")
    print(f"{BColors.WARNING}########################################{BColors.ENDC}")
best = current_population[0]

duration_all = time.time() - start_all_t

################################################################
# Wizualizacja najlepszego rozwiązania w kolejnych pokoleniach #
################################################################
print('Czas wykonywania się całego algorytmu: {:.4f} [s]'.format(duration_all))
plt.plot(best_fitness_individuals)
plt.title('Osiągnięta wartość funkcji J = {:.4f} po wykonaniu {:.1f} iteracji w czasie {:.3f} [s]'.format(our_solution,
                                                                                                          iterations,
                                                                                                          duration_all))
plt.show()
