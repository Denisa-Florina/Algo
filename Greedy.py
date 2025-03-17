#Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate 
#aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.

#De ex. matricea \
#[[1,1,1,1,0,0,1,1,0,1],
#[1,0,0,1,1,0,1,1,1,1],
#[1,0,0,1,1,1,1,1,1,1],
#[1,1,1,1,0,0,1,1,0,1],
#[1,0,0,1,1,0,1,1,0,0],
#[1,1,0,1,1,0,0,1,0,1],
#[1,1,1,0,1,0,1,0,0,1],
#[1,1,1,0,1,1,1,1,1,1]]
#*devine *
#[[1,1,1,1,0,0,1,1,0,1],
#[1,1,1,1,1,0,1,1,1,1],
#[1,1,1,1,1,1,1,1,1,1],
#[1,1,1,1,1,1,1,1,0,1],
#[1,1,1,1,1,1,1,1,0,0],
#[1,1,1,1,1,1,1,1,0,1],
#[1,1,1,0,1,1,1,0,0,1],
#[1,1,1,0,1,1,1,1,1,1]]\


def dfs_ajutator(v,i,j, vizitat):
    if i < 0 or i >= len(v) or j < 0 or j >= len(v[0]):
        return
    
    if v[i][j] == 1 or vizitat[i][j] == 1:
        return

    vizitat[i][j] = 1

    directii = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i1, j1 in directii:
            if i1!=j1 and (i1 == 0 or j1 == 0):
                dfs_ajutator(v,i+i1,j+j1, vizitat)



#Folosesc o metoda greedy, in care marchez toate zerourile conectate de magine
#Inlocuiasc cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
#Parametrii de intrare: v - matrice
#Parametrii de iesire: v - matrice
#Complexitate timp si spatiu O(n*m)
def functia_mea(v):
    n, m = len(v), len(v[0])
    vizitat = [[0] * m for _ in range(n)]
    for i in range(n):
        if v[i][0] == 0:
            dfs_ajutator(v,i,0,vizitat)
        if v[i][m-1] == 0:
            dfs_ajutator(v, i, m-1, vizitat)
    for j in range(m):
        if v[0][j] == 0:
            dfs_ajutator(v, 0, j, vizitat)
        if v[n-1][j] == 0:
            dfs_ajutator(v, n-1, j, vizitat)

    for i in range(n):
        for j in range(m):
            if v[i][j] == 0 and vizitat[i][j] == 0:
                v[i][j] = 1

    return v


#Teste
assert(functia_mea([[1,1,1,1,0,0,1,1,0,1],
                    [1,0,0,1,1,0,1,1,1,1],
                    [1,0,0,1,1,1,1,1,1,1],
                    [1,1,1,1,0,0,1,1,0,1],
                    [1,0,0,1,1,0,1,1,0,0],
                    [1,1,0,1,1,0,0,1,0,1],
                    [1,1,1,0,1,0,1,0,0,1],
                    [1,1,1,0,1,1,1,1,1,1]]) ==  [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                                                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                                                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                                                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                                                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                                                [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                                                [1, 1, 1, 0, 1, 1, 1, 1, 1, 1])

assert(functia_mea([[1,1,0],
                    [1,1,1],
                    [0,1,1]]) == [1,1,1],
                                 [1,1,1],
                                 [1,1,1])

assert(functia_mea([[0,1,1,0],
                    [1,1,1,1],
                    [0,1,1,0]]) == [[0,1,1,0],
                                    [1,1,1,1],
                                    [0,1,1,0]])

assert(functia_mea([[1,1,1],
                    [1,0,1],
                    [1,1,1]]) == [[1,1,1],
                                  [1,1,1],
                                  [1,1,1]])
print("---------------------------------------------------------------------------------------------")



#deepSeek cu deepThink
#Complexitate timp si spatiu O(n*m)
def solve(matrix):
    if not matrix:
        return matrix

    n, m = len(matrix), len(matrix[0])

    def dfs(i, j):
        if i < 0 or i >= n or j < 0 or j >= m or matrix[i][j] != 0:
            return
        matrix[i][j] = '#'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    # Parcurgem marginile și aplicăm DFS pentru a marca '0'-urile de pe margine
    for i in range(n):
        for j in range(m):
            if (i == 0 or i == n-1 or j == 0 or j == m-1) and matrix[i][j] == 0:
                dfs(i, j)

    # Înlocuim toate '0'-urile rămase cu '1'
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            elif matrix[i][j] == '#':
                matrix[i][j] = 0

    return matrix

# Exemplu de utilizare
matrix = [
    [1,1,1,1,0,0,1,1,0,1],
    [1,0,0,1,1,0,1,1,1,1],
    [1,0,0,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,1,1,0,1],
    [1,0,0,1,1,0,1,1,0,0],
    [1,1,0,1,1,0,0,1,0,1],
    [1,1,1,0,1,0,1,0,0,1],
    [1,1,1,0,1,1,1,1,1,1]
]

result = solve(matrix)
for row in result:
    print(row)



def main():
    n = int(input("Introduceti nr de linii: "))
    v = []
    for _ in range(n):
        val = input("Introduceti elementele unei linii: ").split()
        linie = []
        for value in val:
            linie.append(int(value))
        v.append(linie)
    print(functia_mea(v))
main()