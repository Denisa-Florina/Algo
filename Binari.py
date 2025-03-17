#10.
#Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice 
#indexul liniei care conține cele mai multe elemente de 1.

#De ex. în matricea
#[[0,0,0,1,1],
#[0,1,1,1,1],
#[0,0,1,1,1]]
#a doua linie conține cele mai multe elemente 1.


#Functie facuta de mine. Gaseste indexul liniei care conține cele mai multe elemente de 1.
#Parametrii de intrare: v - matrice(lista de liste)
#Parametrii de iesire: int - indexul liniei
#Complexitate de timp O(n*log m); n - nr de linii. m- nr de coloane
#Complexitate de spatiu O(1)
def recv(v):
    low = 0
    high = len(v)

    while low <= high:
        sum = 0
        mid = (high + low) // 2

        for i in range(len(v)):
            sum += v[i][mid]
            if v[i][mid] == 1:
                index = i

        if sum > 1:
            high = mid - 1
        elif sum == 0:
            low = mid + 1
        else:
            return index
        
    return None

#Teste
assert(recv(((0, 0, 0, 1, 1), (0, 1, 1, 1, 1), (0, 0, 1, 1, 1))) == 1)
assert(recv(((0, 0, 0, 1, 1), (0, 1, 1, 1, 1), (1, 1, 1, 1, 1))) == 2)
assert(recv(((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0,0,0,0,1) )) == 3) 
assert(recv(((1, 1, 1), (0, 1, 1), (0, 0, 1))) == 0)  
assert(recv(((0, 0, 0), (0, 0, 1), (1, 1, 1))) == 2) 


#------------------------------------------------------------------------------------------------------------------------------------

#Complexitate de timp O(n*log m); n - nr de linii. m- nr de coloane
#Complexitate de spatiu O(1)
def binary_search(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == 1:
            if mid == 0 or arr[mid - 1] == 0:
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    return -1

def row_with_max_ones(matrix):
    max_ones = 0
    index_of_max_row = -1
    
    for i, row in enumerate(matrix):
        pos = binary_search(row, 0, len(row) - 1)
        
        if pos != -1:
            num_ones = len(row) - pos
            if num_ones > max_ones:
                max_ones = num_ones
                index_of_max_row = i
    
    return index_of_max_row

# Exemplu de utilizare:
matrix = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1]
]

index = row_with_max_ones(matrix)
print(f"Linia cu cele mai multe 1-uri este: {index}")



#----------------------------------------------------------------------------------------------------------------------------------------


def main():
    n = int(input("Introduceti nr de linii: "))
    v = []
    for _ in range(n):
        val = input("Introduceti elementele unei linii: ").split()
        linie = []
        for value in val:
            linie.append(int(value))
        v.append(linie)
    print(recv(v))
main()