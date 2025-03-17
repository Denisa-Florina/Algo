#5. Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} 
#astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare 
#care se repetă. De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.


#Functia mea. Determina valoarea care se repeta din {1, 2, ..., n - 1}
#Parametrii de intrare: v - lista
#Parametrii de iesire: int - nr care se repeta
#Complexitate spatiu O(1)
#Complexitate timp O(n) - n nr de elemente
def functia_mea(v):
    medie = sum(v)
    n=len(v)
    medie_corecta = n*(n-1)/2
    return int(medie - medie_corecta)



#Teste
assert(functia_mea([1,2,3,4,2]) == 2)
assert(functia_mea([5, 1, 2, 3, 4, 5]) == 5)
assert(functia_mea([1, 1]) == 1)
assert(functia_mea([1, 2, 3]) == 3)


#Facuta de ai
#Complexitate timp si spatiu O(n)
def valoare_repetata(sir):
    elemente_intalnite = set()
    
    for numar in sir:
        if numar in elemente_intalnite:
            return numar
        elemente_intalnite.add(numar)
    
    return None 
sir = [1, 2, 3, 4, 2]
print(valoare_repetata(sir))


def main():
    while True:
        v1 = []
        n = int(input("Introduceti dimensiunea vectorului: "))

        if n == 0:
            break
        
        print("Introduceti elementele primului vector:")
        for i in range(n):
            v1.append(int(input(f"{i}: ")))

        print(functia_mea(v1))
main()

