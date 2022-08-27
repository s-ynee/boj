from itertools import combinations_with_replacement
n, m = map(int,input().split())

li = list(range(1,n+1))

nHr = combinations_with_replacement(li,m)
for i in list(nHr):
    for j in i:
        print(j,'',end='')
    print()
