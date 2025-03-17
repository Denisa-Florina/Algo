from collections import deque

def rotate_left(nums, k):
    n = len(nums)
    k = k % n #evitam rotirile inutile
    coada = deque(nums)

    for _ in range(k):
        coada.append(coada.popleft()) #spre stanga
        #coada.appendleft(coada.pop()) dreapta
        
    return list(coada)


print(rotate_left([1, 2, 3, 4, 5], 2))