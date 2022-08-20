import sys
input = sys.stdin.readline

k = int(input())

a = 1
b = 0
if k >= 1:
    for i in range(k):
        m = a+b
        a = b
        b = m

print(a, b)
