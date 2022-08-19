import sys
input = sys.stdin.readline

a = input()
b = input()

phone = ""

for i in range(len(a)):
    phone += a[i]
    phone += b[i]

phone = phone[:-2]

while True:
    front = phone[:-1]
    back = phone[1:]
    o =""
    for j,k in zip(front,back):
        x = int(j) + int(k)
        o += str(x%10)
    phone = o
    if len(phone) == 2:
        break

print(o)
    






