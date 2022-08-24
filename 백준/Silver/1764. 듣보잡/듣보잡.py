n,m = map(int,input().split())
li =[]
a,b = [],[]

for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append((input()))

intersection = list(set(a) & set(b))
intersection.sort()
print(len(intersection))
for i in intersection:
    print(i)






