#9.
# Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din 
#coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)), să se calculeze suma elementelor 
#din sub-matricile identificate de fieare pereche.

#De ex, pt matricea
#[[0, 2, 5, 4, 1], 12
#[4, 8, 2, 3, 7], 24
#[6, 3, 4, 6, 2], 13
#[7, 3, 1, 8, 3],
#[1, 5, 7, 9, 4]]
#și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), suma elementelor din prima 
# sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.

#p=(1,1)
#q=(3,3)
#Functia mea. Determina suma elementelor din submatricea det de 2 coordonate
#Parametrii de intrare: p-(int, int), q-(int, int), v-matrice
#Parametrii de iesire: suma-int
#Complexitate timp: O(n*m), n,m dimensiunile sub-matricei
#Complexitate spatiu: O(1)
def functia_mea(p,q,v):
    suma=0
    for i in range(p[0],q[0]+1):
        for j in range(p[1],q[1]+1):
            suma+=v[i][j]
    return suma

#Functia mea. Determina suma elementelor din submatricea det de o lista de coordonate
#Parametrii de intrare: l-lista de liste care contine 2 perechi de int-uri, v-matrice
#Parametrii de iesire: suma-int
#Complexitate timp: O(n*m*p), n,m dimensiunile sub-matricei, p-nr de perechi
#Complexitate spatiu: O(p), p-nr de perechi
def main_fmea(l,v):
    suma = []
    for p in l:
        suma.append(functia_mea(p[0],p[1],v))
    return suma


#Teste
assert(functia_mea((1,1),(3,3),((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==38)
assert(functia_mea((2, 2),(4, 4),((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==44)
assert(main_fmea([((1, 1), (3, 3)), ((2, 2), (4, 4))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[38, 44])
assert(main_fmea([((1, 1), (1,1)), ((2, 2), (2,2))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4))) == [8,4])
assert(main_fmea([((2,2), (2,4)), ((1,3), (2,4))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[12, 18])

 
#----------------------------------------------------------------------------------------------------------------------------------------------

#Facuta de ai
#Complexitate timp: O(n*m*p), n,m dimensiunile sub-matricei, p-nr de perechi
#Complexitate spatiu: O(p), p-nr de perechi
def compute_submatrix_sums(matrix, pairs):
    results = []
    for (p, q), (r, s) in pairs:
        submatrix_sum = sum(
            matrix[i][j] for i in range(p, r + 1) for j in range(q, s + 1)
        )
        results.append(submatrix_sum)
    return results

# Exemplu de utilizare:
matrix = [
    [0, 2, 5, 4, 1],
    [4, 8, 2, 3, 7],
    [6, 3, 4, 6, 2],
    [7, 3, 1, 8, 3],
    [1, 5, 7, 9, 4]
]

pairs = [((1, 1), (3, 3)), ((2, 2), (4, 4))]

sums = compute_submatrix_sums(matrix, pairs)
print(sums)  # Output: [38, 44]



#----------------------------------------------------------------------------------------------------------------------------------------------


#Metoda mai eficienta - folosim o matrice de sume a sub-matricilor
#Functia mea. Determina suma elementelor din submatricea det de o lista de coordonate
#Parametrii de intrare: l-lista de liste care contine 2 perechi de int-uri, v-matrice
#Parametrii de iesire: suma-int
#Complexitate timp O(n*m+p), n,m dimensiunile sub-matricei, p-nr de perechi
#Complexitate spatiu O(n^2)
def constr_matrice(l,v):
    m = [[0] * len(v[0]) for _ in range(len(v))]

    for i in range(0,len(v)):
        for j in range(0,len(v[0])):
            suma = v[i][j]
            if i > 0:
                suma += m[i-1][j]
            if j > 0:
                suma += m[i][j-1]
            if i > 0 and j > 0:
                suma -= m[i-1][j-1]
            m[i][j]=suma
    #print(m)

    res=[]
    for p in l:
        x1=p[0][0]
        y1=p[0][1] 
        x2=p[1][0]
        y2=p[1][1]
        suma = m[x2][y2] - m[x2][y1-1] - m[x1-1][y2] + m[x1-1][y1-1]
        res.append(suma)
    return res

#Teste
assert(constr_matrice([((1, 1), (3, 3)), ((2, 2), (4, 4))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[38,44])
assert(constr_matrice([((1, 1), (1,1)), ((2, 2), (2,2))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4))) == [8,4])
assert(constr_matrice([((0,0), (4,4)), ((2, 2), (3,3)), ((1, 1), (2,2)) ],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[0, 19, 17])
assert(constr_matrice([((0,0), (1,1)), ((2, 3), (2,4))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[44, 8])
assert(constr_matrice([((2,2), (2,4)), ((1,3), (2,4))],((0, 2, 5, 4, 1),(4, 8, 2, 3, 7),(6, 3, 4, 6, 2),(7, 3, 1, 8, 3),(1, 5, 7, 9, 4)))==[12, 18])

 
#----------------------------------------------------------------------------------------------------------------------------------------------



def main():
    
    n = int(input("Introduceti nr de perechi: "))
    l = []
    for i in range(n):
        input_values = input("Introduceti perechile cu spatiu: ").split()
        x1 = int(input_values[0])
        y1 = int(input_values[1])
        x2 = int(input_values[2])
        y2 = int(input_values[3])
        l.append([(x1, y1), (x2, y2)])

    n = int(input("Introduceti nr de linii: "))
    v = []
    for i in range(n):
        val = input("Introduceti elementele unei linii: ").split()
        linie = []
        for value in val:
            linie.append(int(value))
        v.append(linie)

    print(constr_matrice(l, v))

main()

