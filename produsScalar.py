#3.Să se determine produsul scalar a doi vectori rari care conțin numere reale. 
#Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea 
#oricâte dimensiuni. De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.


#Functie facuta de AI
#Complexitate timp O(n) si spatiu O(1)
def produs_scalar(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectorii trebuie să aibă aceeași dimensiune.")
    produs = 0
    for i in range(len(v1)):
        produs += v1[i] * v2[i]
    return produs

v1 = [1, 0, 2, 0, 3]
v2 = [1, 2, 0, 3, 1]

rezultat = produs_scalar(v1, v2)
print(f"Produsul scalar este: {rezultat}")


#Functia facuta de mine
#Calculeaza produsul scalar a doi vectori
#Parametrii de intrare: v1, v2 - doua liste
#Parametrii de iesire: int - produsul scalar
#Complexitate timp O(k), unde k este numarul de elemente nenule din vectori
#Complexitate spatiu O(1)
def functia_mea(v1, v2):
    suma = 0
    i=0
    while i < len(v1):
        while i<len(v1) and (v1[i] == 0 or v2[i] == 0) :
            i += 1
        if i<len(v1):
            suma += v1[i]*v2[i]
            i+=1
    return suma


#Teste
assert(functia_mea([1,0,2,0,3],[1,2,0,3,1]) == 4)
assert(functia_mea([1, 2, 3], [4, 5, 6]) == 32)  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
assert(functia_mea([0, 0, 0], [0, 0, 0]) == 0)
assert(functia_mea([1, 0, 0], [0, 0, 2]) == 0)  # 1*0 + 0*0 + 0*2 = 0
assert(functia_mea([1, 2, 0, 4, 0, 0], [0, 3, 0, 5, 0, 0]) == 26)  # 1*0 + 2*3 + 0*0 + 4*5 + 0*0 + 0*0 = 0 + 6 + 0 + 20 + 0 + 0 = 26
assert(functia_mea([3], [4]) == 12)


def main():
    while True:
        n = int(input("Introduceti dimensiunea vectorilor: "))

        if n == 0:
            break

        v1 = []
        v2 = []

        print("Introduceti elementele primului vector:")
        for i in range(n):
            v1.append(int(input(f"{i}: ")))

        print("Introduceti elementele celui de-al doilea vector:")
        for i in range(n):
            v2.append(int(input(f"{i}: ")))
            
        print(functia_mea(v1, v2))
#main()
