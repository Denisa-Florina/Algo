#2.Să se determine distanța Euclideană între două locații identificate 
#prin perechi de numere. De ex. distanța între (1,5) și (4,1) este 5.0

import numpy
import math


#Funtia(facuta de mine) calculeaza distanța Euclideană între două locații identificate
#Parametrii de intrare: int x1-primul nr din prima pereche
#                       int y1-al doilea nr din prima pereche
#                       int x2-primul nr din a doua pereche
#                       int y2-al doilea nr din a doua pereche
#Parametrii de iesire: float-distanta Euclideana
#Complexitate timp si spatiu O(1)
def functia_mea(x1, y1, x2, y2):
    m1 = (y1 - y2)**2
    m2 = (x1 - x2)**2
    suma = m1+m2
    return numpy.sqrt(suma)


#Functie facuta de AI
#Complexitate timp si spatiu O(1)
def distanta_euclidiana(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
punct1 = (1, 5)
punct2 = (4, 1)
print(f"Distanța Euclidiană este: {distanta_euclidiana(punct1, punct2)}")


#Teste
assert(functia_mea(1,5,4,1) == 5)
assert(functia_mea(1,5,1,4) == 1)
assert(functia_mea(1,3,1,4) == 1)



def main():
    while True:
        text = input("Introduce-ti 0 pentru exit: ")
        if text == '0':
            break
        x1 = int(input("X1: "))
        y1 = int(input("Y1: "))
        x2 = int(input("X2: "))
        y2 = int(input("Y1: "))
        print(functia_mea(x1,y1,x2,y2))
main()