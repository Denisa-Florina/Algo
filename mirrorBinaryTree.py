from collections import deque

class Nod:
    def __init__(self, valoare):
        self.valoare = valoare
        self.stang = None
        self.drept = None
    

def creeaza_arbore(lst):
    if not lst or lst[0] == '*':
        return None
    
    root = Nod(lst[0])
    coada = deque([root])
    index = 1

    while coada and index <= len(lst):
        nod_current = coada.popleft()

        if index < len(lst) and lst[index] != '*':
            nod_current.stang = Nod(lst[index])
            coada.append(nod_current.stang)
        index += 1

        if index < len(lst) and lst[index] != '*':
            nod_current.drept = Nod(lst[index])
            coada.append(nod_current.drept)
        index += 1

    return root

def mirror(root):
    if not root:
        return
    
    root.stang, root.drept = root.drept, root.stang

    mirror(root.stang)
    mirror(root.drept)

def creeaza_lista(root:Nod):
    if not root:
        return []
    
    result = []
    coada = deque([root])
    result.append(root.valoare)

    while coada:
        nod_current = coada.popleft()

        if nod_current.stang:
            result.append(nod_current.stang.valoare)
            coada.append(nod_current.stang)
        else:
            result.append('*')

        if nod_current.drept:
            result.append(nod_current.drept.valoare)
            coada.append(nod_current.drept)
        else:
            result.append('*')

    return result

def main(lst):
    root = creeaza_arbore(lst)
    mirror(root)
    print(creeaza_lista(root))



def face_oglindit(lst):
    i = 0
    a = 0
    result = []
    while a+2**i <= len(lst):
        for k in range(2**i):
            result.append(lst[a+2**i-k-1])
        i += 1
        a = 2**i-1
    return result



def verifica_oglindit(lst):
    i=0
    a=0
    while a+i**2 <= len(lst):
        for k in range(2**i//2):
            if(lst[a+2**i-k-1] != lst[a+k]):
                return False
        i += 1
        a = 2**i-1
    return True


print(verifica_oglindit([3,2,2,1,3,3,1, '*', 6, '*', 11, 11, '*', 6, '*']))

#     1  3  2  6  *   5   4
#                    0   1  2   3  4  5   6    7   8   9   10   11  12   13   14
print(face_oglindit([3,2,2,1,3,3,1, '*', 6, '*', 11, 11, '*', 6, '*']))
#                   [10, 15, 5, 20, 12, 7, 3,| '*', '*', '*', 11, '*', '*', 6, '*']
#                   a=0  a=1    a=2           a=6  
