n = int(input())
m = int(input())
li =[]

for i in range(n,m+1):
    pm = True
    if i == 1:
        pm = False
        pass


    for j in range(2,i):
        if i%j == 0:
            pm = False
    if pm == True:
            li.append(i)

if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])