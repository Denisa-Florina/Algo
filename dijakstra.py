import heapq

def dijkstra(rad, adj):
    pq = [(0, rad)]  # (cost, node)
    dist = {node: float('inf') for node in adj}
    parinti = {node: None for node in adj}
    
    dist[rad] = 0
    
    while pq:
        cost, nod_curent = heapq.heappop(pq)
        
        if cost > dist[nod_curent]:
            continue
        
        for vecin, cost_vecin in adj[nod_curent]:
            if dist[nod_curent] + cost_vecin < dist[vecin]:
                dist[vecin] = dist[nod_curent] + cost_vecin
                parinti[vecin] = nod_curent
                heapq.heappush(pq, (dist[vecin], vecin))
    
    return parinti, dist

def main():
    n, m = map(int, input().split())
    
    adj = {}
    for _ in range(m):
        x, y, cost = input().split()
        cost = int(cost)
        if x not in adj:
            adj[x] = []
        if y not in adj:
            adj[y] = []
        adj[x].append((y, cost))
        adj[y].append((x, cost))
    
    start, end = input().split()
    parinti, dist = dijkstra(start, adj)
    
    if end not in parinti or parinti[end] is None:
        print("IMPOSSIBLE")
        return
    
    drum = []
    while end is not None:
        drum.append(end)
        end = parinti[end]
    
    print(dist[drum[0]])
    print(" ".join(drum[::-1]))

main()
