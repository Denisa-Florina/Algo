import sys
sys.setrecursionlimit(10**8) 

def dfs(adj, rad, viz):
    if rad in viz:
        return
    
    viz.append(rad)

    for e in adj[rad]:
        dfs(adj, e, viz)



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
  

    vizitat_total=[]
    componente = []
    for i in range(1, n+1):
        if i not in vizitat_total:
            dfs(adj, i, vizitat_total)
            componente.append(i)

    adaugate=[]
    for i in range(1, len(componente)):
        muchie = []
        muchie.append(componente[i-1])
        muchie.append(componente[i])
        adaugate.append(muchie)

    print(len(adaugate))
    for e in adaugate:
        print(str(e[0]) + " " + str(e[1]))


main()

