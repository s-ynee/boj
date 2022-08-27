from itertools import permutations
n,m = map(int,input().split())
li = list(range(1,n+1))


nPr = permutations(li,m)

for i in list(nPr):
    for j in i:
        print(j, '',end='')
    print()

