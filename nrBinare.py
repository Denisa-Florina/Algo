#8.Să se genereze toate numerele (în reprezentare binară) cuprinse între 1 și n. De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.


#Genereza toate numerele (în reprezentare binară) cuprinse între 1 și n.
#Parametrii de intrare: n - int 
#Parametrii de iesire string
#Complexitate timp O(n), n - ne de elemente
#Complexitate spatiu: O(1)
def functia_mea(n):
    s = ""
    for i in range(1,n+1):
        nr = bin(i)
        nr = nr[2:]
        s += nr + " "
    return s

#Teste
assert(functia_mea(4)=='1 10 11 100 ')
assert(functia_mea(3) == '1 10 11 ')
assert(functia_mea(5) == '1 10 11 100 101 ')
assert(functia_mea(6) == '1 10 11 100 101 110 ')
assert(functia_mea(10) == '1 10 11 100 101 110 111 1000 1001 1010 ')

#Facuta de ai
#Complexitate timp si spatu O(n), n nr de elemente
def generare_binare(n):
    binare = []
    for i in range(1, n + 1):
        binare.append(bin(i)[2:])
    return binare
n = 4
print(generare_binare(n))  # Va afișa ['1', '10', '11', '100']


def main():
    while True:
        text = input("Introduce-ti 0 pentru exit: ")
        if text == '0':
            break
        x1 = int(input("N: "))
        print(functia_mea(x1))
main()
