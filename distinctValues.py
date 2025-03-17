from collections import Counter

def main():
    n = 5
    k = 2
    v = [1,2,3,1,1]

    distincte = 0
    if k >= 1:
        distincte += n

    cnt = {}
    cnt[v[0]] = 1
    dist = 1
    for i in range(1, len(v)):
        if v[i] in cnt:
           if(dist + 1 <= k):
                v[i] += 1
        else:
           v[i] = 1

main()
    