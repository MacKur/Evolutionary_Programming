# GeneticAlgorithms2020
The task of pushing a cart using Evolutionary Programming

## Pytania i odpowiedzi:
- Jakie ograniczenia dla u? Od 0 do 100? Od 0 do 10.0?

- Czy powinniśmy traktować U jako sterowanie i nasza populację? Czy traktować J jako Fit?

![AG](https://user-images.githubusercontent.com/29255453/100860091-591deb00-3490-11eb-99f5-20edd2091829.PNG)

- Przykład: N = 3 
- 1sza iteracja!
- Wybieramy populacje u_0 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
- Liczymy x_2 dla całej populacji dla k = 0, k = 1, k = 2 (do N-1)
- Mając x_2(k=2) obliczamy J dla każdego osobnika z populacji u_0
- I wybieramy J_max spośród powyższych i zapisujemy je na wykresie 

![image](https://user-images.githubusercontent.com/28922780/100869183-f2eb9500-349c-11eb-87d0-a04b061dcb92.png)

## Schemat 
![AG1](https://user-images.githubusercontent.com/29255453/100860591-fd079680-3490-11eb-8290-0ba06040b792.PNG)
![AG2](https://user-images.githubusercontent.com/29255453/100860590-fc6f0000-3490-11eb-94e7-94d3fa9c8cd8.PNG)
![AG3](https://user-images.githubusercontent.com/29255453/100860593-fd079680-3490-11eb-9c66-0fb407f43aa6.PNG)

## Towardsdatascience examples
- DEAP > https://towardsdatascience.com/genetic-algorithms-in-python-using-the-deap-library-e67f7ce4024c

- DEAP > https://towardsdatascience.com/intro-to-evolutionary-computation-using-deap-618ca974b8cb

- ABC module > https://towardsdatascience.com/an-extensible-evolutionary-algorithm-example-in-python-7372c56a557b

- Evolution module > https://github.com/Garve/Evolutionary-Algorithm

## DEAP documentation
https://deap.readthedocs.io/en/master/

## Pyvolution documentation
https://pyvolution.readthedocs.io/en/latest/index.html

