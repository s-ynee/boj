n = int(input())

a = list(map(int,input().split()))

m = int(input())

b = list(map(int,input().split()))

intersection = list(set(a) & set(b))
for i in b:
    if i in intersection:
        print(1)
    else:
        print(0)