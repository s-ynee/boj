import sys
import bisect

input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))

m = int(input())
b = list(map(int,input().split()))
a_s = sorted(a)

p =[]
for i in b:
    c = bisect.bisect_left(a_s,i)
    d = bisect.bisect_right(a_s,i)
    out = d-c
    p.append(out)
print(*p)