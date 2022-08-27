from itertools import product
n, m = map(int,input().split())

li = list(range(1,n+1))

nPir = product(li,repeat = m)
for i in list(nPir):
    for j in i:
        print(j,'',end='')
    print()
