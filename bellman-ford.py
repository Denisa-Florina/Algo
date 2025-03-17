def bellman_ford(rad, adj, nodes):
    dist = {node: float('inf') for node in nodes}
    parinti = {node: None for node in nodes}
    
    dist[rad] = 0
    
    for _ in range(len(nodes) - 1):
        for node in adj:
            for vecin, cost in adj[node]:
                if dist[node] + cost < dist[vecin]:
                    dist[vecin] = dist[node] + cost
                    parinti[vecin] = node
    
    for node in adj:
        for vecin, cost in adj[node]:
            if dist[node] + cost < dist[vecin]:
                print("Negative cycle detected")
                return None, None
    
    return parinti, dist

def main():
    n, m = map(int, input().split())
    
    adj = {}
    nodes = set()
    for _ in range(m):
        x, y, cost = input().split()
        cost = int(cost)
        if x not in adj:
            adj[x] = []
        if y not in adj:
            adj[y] = []
        adj[x].append((y, cost))
        nodes.add(x)
        nodes.add(y)
    
    start, end = input().split()
    
    parinti, dist = bellman_ford(start, adj, nodes)
    
    if parinti is None or end not in parinti or parinti[end] is None:
        print("IMPOSSIBLE")
        return
    
    drum = []
    while end is not None:
        drum.append(end)
        end = parinti[end]
    
    print(dist[drum[0]])
    print(" ".join(drum[::-1]))

main()