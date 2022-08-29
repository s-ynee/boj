s = input()
li = []
for i in range(len(s)):
    for j in range(len(s)-i):
        li.append(s[i:i+j+1])
li = list(set(li))

print(len(li))