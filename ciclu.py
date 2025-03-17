ok = 0

def dfs(parinti, adj, rad, vizitat, result):
    global ok
    if rad in vizitat and ok == 0:
        return
    
    vizitat.append(rad)
    result.append(rad)

    for e in adj[rad]:
        if e in vizitat and parinti[rad] != e and parinti[rad] !=-1 and ok == 0:
            ok = 1
            nr = 1
            string = str(e) + " "
            for i in result[::-1]:
                nr += 1
                string+=str(i) + " "
                if(i == e):
                    break
            print(nr)
            print(string)

        if e not in vizitat and ok == 0:
            parinti[e] = rad
            dfs(parinti, adj, e, vizitat, result)
        
    result.remove(rad)


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
  

    parinti = [-1] * (n+1)
    vizitat_total = []
    for i in range(1, n+1):
        if i not in vizitat_total:
            dfs(parinti, adj, i, vizitat_total, [])
            if ok == 1:
                return
            
    print('IMPOSSIBLE')

main()
            
