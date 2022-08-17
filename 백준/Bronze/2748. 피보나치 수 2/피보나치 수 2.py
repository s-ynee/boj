import sys

input = sys.stdin.readline()

n = int(input)

front = 0
next = 1

if n == 0:
    out = 0
elif n == 1:
    out = 1
else:
    for i in range(n-1):
        out = front + next
        front = next
        next = out



number = out
print(number)