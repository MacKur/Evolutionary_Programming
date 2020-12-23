import time
import numpy as np
import matplotlib.pyplot as plt
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



def fitness_function(_N, population):
    all_fitness = []
    u = []
    arr = []
    x1 = 0
    x2 = 0
    sum_u = 0
    k = 0
    # print('len population', len(population))
    for osobnik in population:
        a = 0
        b = 20
        arr.clear()
        u.clear()
        # print('osobnik', osobnik)
        osobnik = osobnik * values
        # print('osobnik x values', osobnik)
        for j in range(N):
            arr.append(osobnik[a:b])
            a = a + 20
            b = b + 20
            # v1 u.append(round(np.sum(arr[j]), 3))
            u.append(np.sum(arr[j]))
        #print('arr', arr)
        # print('u', u)
        for k in range(0, _N):
            x1_new = x2
            # v1 x2_new = round(2 * x2 - x1 + 1 / (N ** 2) * u[k], 3)
            x2_new = 2 * x2 - x1 + 1 / (N ** 2) * u[k]
           # print(f"x2_new = 2* {x2} - {x1} + {u[k]} / {N}**2")
            sum_u = sum_u + (u[k] ** 2)
            x1 = x1_new
            x2 = x2_new
            # print('sum_u', sum_u)
            # print(f"x1({k}) = {x1}")
            # print(f"x2({k}) = {x2}", end="\n\n")
        J = x1 - sum_u / (2 * _N)
        sum_u = 0
        x2 = 0
        x1 = 0
        # print('J', J)
        all_fitness.append(J)
    best_Js.append(max(all_fitness))
    return all_fitness


def sort_by_fitness(arr):
    return arr[1]


def make_new_population(current_population):
    mutated_population = []
    # print('len current pop', len(current_population))
    mutated_population.clear()
    # print(current_population[0])
    for man in current_population:
        new_man = []
        for bit in man:
            z = random.random()
            if z < epsilon:
                new_man.append(int(not bit))
            else:
                new_man.append(bit)
        mutated_population.append(new_man)

    mutated_population = np.array(mutated_population)
    # print('len mutated pop', len(mutated_population))
    # print('mutants array', mutated_population)

    whole_population = np.concatenate((current_population, mutated_population))
    # print('whole_population', whole_population)

    fitness_array = fitness_function(N, whole_population)
    # print('fitnessarray', fitness_array)
    # print("size_fitnessarr", len(fitness_array))
    # print('sorted', sorted(fitness_array))
    zipped = zip(whole_population, fitness_array)
    zipped_sorted = sorted(zipped, key=sort_by_fitness,
                           reverse=True)  # sortujemy od najlepszych osobników żeby uciąć 100 najgorszych
    bests = zipped_sorted[:len(zipped_sorted) // 2]  # tutaj obcinamy dolną połowę rozwiązań
    # print('bests', bests)  # tutaj mamy array w formie array([0, 1, 0, 1 ..., 1, 0]), FITNESS), od najlepszego do najgorszego 100 osobników
    new_p = [x[0] for x in bests]  # to wyżej to jest krok 7 , my możemy dodać przed tym metodę turniejową w której brać będziemy
    new_p = np.array(new_p)  # dobierać osobników w 40 grupo po 5 osobników i segregować ich fitnessami w tych grupach, na tej postawie
    # print('new_p', new_p)

    return new_p


size_of_population = 70
epsilon = 0.2
iterations = 5000
N = 5  # parameter from exercise
# values = np.random.uniform(0, 1, 20*N)

values = []
best_Js = []
# Set a length of the list to 10
for i in range(0, 20 * N):
    # any random float between 50.50 to 500.50
    # don't use round() if you need number as it is
    # v1 x = round(random.uniform(0, 0.1), 3)
    x = random.uniform(0, 0.1)
    values.append(x)

# values = float("{:.3f}".format(values_x))
# values = np.random.randint(0, 10, 20*N)

# print('values', values)
# print('len(values): ', len(values))

starting_population = np.random.randint(0, 2, (size_of_population, 20 * N))
current_population = starting_population
# print('current_population', current_population)
start_all_t = time.time()
for i in range(iterations):
    start_t = time.time()
    new_population = make_new_population(current_population)
    duration = time.time() - start_t
    #  print('new_population', new_population)
    current_population = new_population
    print("\n" + bcolors.OKGREEN + f"==========================================\n\t\tITERATION NR:\t{i}\n==========================================\n" + bcolors.ENDC)
    print('Processing time: {:.4f}'.format(duration))

best = current_population[0]
duration_all = time.time() - start_all_t
print('Processing time of full program: {:.4f}'.format(duration_all))
plt.plot(best_Js)
# plt.figtext(0.5, 0.01, "one text and next text", ha="center", fontsize=6)
plt.show()
