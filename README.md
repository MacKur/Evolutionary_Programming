# Evolutionary Programming
The task of pushing a cart using Evolutionary Programming

## Temat projektu
![image](https://raw.githubusercontent.com/MacKur/Evolutionary_Programming/main/images%2Bresults/Polecenie.PNG)

## Schemat tworzonego algorytmu
![image](https://raw.githubusercontent.com/MacKur/Evolutionary_Programming/main/images%2Bresults/Schemat.png)

## Wyjaśnienie implementacji oraz zastosowanego algorytmu ewolucyjnego
### Kodowanie
Przed rozpoczęciem pracy algorytmu generowana jest lista losowych wartości z przedziału od 0 do 0.1 co w pewnym stopniu nakłada ograniczenie na wartości które mogą przyjąć sterowania u:

### Populacja 
Składa się z 70 osobników zgodnie z informacjami podanymi w książce Algorytmy genetyczne + struktury danych = programy ewolucyjne, Z. Michalewicz WNT, Warszawa, wyd. 2, 1999. Każdy z osobników składa się z 20 * N genów o allelach należących do dwuelementowego zbioru liczb {0, 1}. Co pozwala w późniejszym etapie na zastosowanie prostej strategii mutacyjnej. 

### Dekodowanie 
Każde 20 kolejnych bitów przemnożonych przez listę wartości values po zsumowaniu tworzy  pojedynczy krok sterowania u.

### Mutacja
Polega na zmianie wartości bitów chromosomu osobnika w przypadku spełnienia warunku podanego w linii 98.

### Selekcja 
Do kolejnej populacji wybierana jest lepsza połowa ze 140 osobników na których składa się 70 osobników rodzicielskich oraz 70 potomków (osobników po mutacji).

## Rezultaty działania programu

### Konsola
![image](https://raw.githubusercontent.com/MacKur/Evolutionary_Programming/main/images%2Bresults/Sample_result_console.PNG)

### Wykres
![image](https://raw.githubusercontent.com/MacKur/Evolutionary_Programming/main/images%2Bresults/Sample_result.png)


## Towardsdatascience examples
- DEAP > https://towardsdatascience.com/genetic-algorithms-in-python-using-the-deap-library-e67f7ce4024c

- DEAP > https://towardsdatascience.com/intro-to-evolutionary-computation-using-deap-618ca974b8cb

- ABC module > https://towardsdatascience.com/an-extensible-evolutionary-algorithm-example-in-python-7372c56a557b

- Evolution module > https://github.com/Garve/Evolutionary-Algorithm

## DEAP documentation
https://deap.readthedocs.io/en/master/

## Pyvolution documentation
https://pyvolution.readthedocs.io/en/latest/index.html

