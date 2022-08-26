import itertools
n = int(input())

li = list(range(1,n+1))
nPr = itertools.permutations(li,n)

for i in list(nPr):
    for j in i:
        print(j, '',end='')
    print()