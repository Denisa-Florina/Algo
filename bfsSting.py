from collections import deque

def bfs(rad, adj):
    coada = deque([rad])
    dist = {node: float('inf') for node in adj}
    parinti = {node: None for node in adj}
    
    dist[rad] = 0
    parinti[rad] = None

    while coada:
        nod_curent = coada.popleft()

        for e in adj[nod_curent]:
            if dist[e] > dist[nod_curent] + 1:
                dist[e] = dist[nod_curent] + 1
                parinti[e] = nod_curent
                coada.append(e)

    return parinti

def main():
    n, m = map(int, input().split())
    
    adj = {}
    for _ in range(m):
        x, y = input().split()
        if x not in adj:
            adj[x] = []
        if y not in adj:
            adj[y] = []
        adj[x].append(y)
        adj[y].append(x)
    
    start, end = input().split()
    parinti = bfs(start, adj)
    
    if end not in parinti or parinti[end] is None:
        print("IMPOSSIBLE")
        return
    
    drum = []
    while end is not None:
        drum.append(end)
        end = parinti[end]
    
    print(len(drum))
    print(" ".join(drum[::-1]))

main()