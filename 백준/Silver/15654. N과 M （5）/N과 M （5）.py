from itertools import permutations
n, m = map(int,input().split())
li= list(map(int,input().split()))

li.sort()
nPr = permutations(li,m)
for j in list(nPr):
    for k in j:
        print(k,'',end='')
    print()
    