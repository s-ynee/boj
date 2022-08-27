from itertools import combinations
n, m = map(int,input().split())

li = list(range(1,n+1))
nCr = combinations(li, m)

for i in list(nCr):
    for j in i:
        print(j,'',end='')
    print()