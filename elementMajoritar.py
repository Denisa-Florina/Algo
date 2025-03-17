#6.Pentru un șir cu n numere întregi care conține și duplicate, să se determine 
#elementul majoritar (care apare de mai mult de n / 2 ori). De ex. 2 este elementul 
#majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].


#Functia mea. Determina elementul majoritar
#Parametrii de intrare v - lista
#Parametrii de iesire int - nr majoritar
#Complexitate timp si spatu O(n), n nr de elemente
from collections import Counter
def functia_mea(v):
    frecventa = Counter(v)
    nr = frecventa.most_common(1)[0][0]
    frec = frecventa.most_common(1)[0][1]
    if frec >= len(v) // 2:
        return nr
    else:
        return None

#Teste
assert(functia_mea([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])==2)
assert(functia_mea([1, 1, 1, 1, 2, 3, 3, 3]) == 1)
assert(functia_mea([9, 9, 9, 9, 9, 2, 2]) == 9)
assert(functia_mea([10, 20, 30, 30, 30, 20, 20]) == 20)


#Algoritmul Boyer-Moore Majority Vote
#Complexitate spatiu O(1)
#Complexitate timp O(n) 
def element_majoritar(sir):
    candidat = None
    contor = 0
    for numar in sir:
        if contor == 0:
            candidat = numar
        contor += (1 if numar == candidat else -1)

    aparitii = sir.count(candidat)
    if aparitii > len(sir) // 2:
        return candidat
    return None 

sir = [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2] 
print(element_majoritar(sir))


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
