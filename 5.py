def tspdp(c,tour,start,n):
    mincost=999
    ccost=-200
    temp = [None] * n
    mintour = [None] * n
    if(start==n-2):
        return c[tour[n-2]][tour[n-1]]+c[tour[n-1]][0]
    for i in range(start+1,n):
        for j in range(n):
            temp[j]=tour[j]
        temp[start+1]=tour[i]
        temp[i]=tour[start+1]
        ccost=tspdp(c,temp,start+1,n)
        if(c[tour[start]][tour[i]]+ccost) < mincost:
            mincost=c[tour[start]][tour[i]]+ccost
            for j in range(n):
                mintour[j]=temp[j]
        for j in range(n):
            tour[j]=mintour[j]
    return mincost

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [10, 25, 30, 0]]
n = len(graph)
if n == 1:
    print("Path is not possible")
    exit()

tour = list(range(n))
cost=tspdp(graph,tour,0,n)
for i in range(n):
    print(tour[i],"-------->", end = '')
print("0")
print("The minimum cost is",cost)