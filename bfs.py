from collections import deque

def bfs(rad, adj, n):
    coada = deque([rad])
    dist = [1000000007] * (len(adj)+1)
    parinti = [-1] * (len(adj)+1)
    dist[rad] = 0
    parinti[rad] = 0

    while coada:
        nod_curent = coada.popleft()

        for e in adj[nod_curent]:
            if dist[e] > dist[nod_curent] + 1:
                dist[e] = dist[nod_curent] + 1
                parinti[e] = nod_curent
                coada.append(e)

    return parinti

def main():
    text = input().split(' ')
    n= int(text[0])
    m= int(text[1])

    adj = {i: [] for i in range(1, n+1)}

    for _ in range(m):
        text = input().split(' ')
        x= int(text[0])
        y= int(text[1])
        adj[x].append(y)
        adj[y].append(x)

    parinti = bfs(1, adj, n)
    drum=[]

    if parinti[n] == -1:
        print('IMPOSSIBLE')
        return
    
    while n != 0:
        drum.append(n)
        n = parinti[n]
    
   
    print(len(drum))
    string = ""
    for e in drum[::-1]:
        string += str(e) + " "
    print(string)


main()