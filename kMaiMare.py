#7.Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n). 
#De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.
from collections import Counter


#Determina al k-lea cel mai mare element
#Parametrii de intrare: v - lista, k - int 
#Parametrii de iesire int - elementul k  maxim 
#Complexitate timp O(n*k), n - ne de elemente
#Complexitate spatiu: O(1)
def functia_mea(v, k):
    while k>0 and v!=[]:
        maxi = max(v)
        k -= 1
        if k == 0:
            return maxi
        v.remove(maxi)
    return None


#Teste
assert(functia_mea([7,4,6,3,9,1], 2)==7)
assert(functia_mea([7, 4, 6, 3, 9, 1], 2) == 7)
assert(functia_mea([7, 4, 6, 3, 9, 1], 3) == 6)
assert(functia_mea([7, 4, 6, 3, 9, 1], 4) == 4)
assert(functia_mea([7, 4, 6, 3, 9, 1], 5) == 3) 



#Facuta de AI
#Complexitate timp: O(n*log(n))
#Complexitate spatiu: O(n), n - nr de elemente
def al_klea_cel_mai_mare_element(sir, k):
    sir_sortat = sorted(sir, reverse=True)
    return sir_sortat[k-1]

# Exemplu de utilizare
sir = [7, 4, 6, 3, 9, 1]
k = 2
print(al_klea_cel_mai_mare_element(sir, k))  # Va afișa 7




#Determina al k-lea cel mai mare element
#Parametrii de intrare: v - lista, k - int 
#Parametrii de iesire int - elementul k  maxim 
#Complexitate timp: O(n*logn), n - ne de elemente
#Complexitate spatiu: O(n)
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    swap(arr, i + 1, high)
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def functia_mea_imbunatatita(v, k):
    n = len(v)
    quickSort(v,0,n-1)
    return v[n-k]


#Teste
assert(functia_mea_imbunatatita([7, 4, 6, 3, 9, 1], 2) == 7)
assert(functia_mea_imbunatatita([7, 3, 6, 2, 9, 0], 3) == 6)
assert(functia_mea_imbunatatita([7, 4, 6, 2, 9, 2], 4) == 4)
assert(functia_mea_imbunatatita([7, 5, 6, 3, 8, 1], 5) == 3) 



def main():
    while True:
        v1 = []
        k = int(input("Introduceti k: "))
        n = int(input("Introduceti dimensiunea vectorului: "))

        if n == 0:
            break
        
        print("Introduceti elementele primului vector:")
        for i in range(n):
            v1.append(int(input(f"{i}: ")))

        #print(functia_mea(v1, k))
        print(functia_mea_imbunatatita(v1, k))
main()
