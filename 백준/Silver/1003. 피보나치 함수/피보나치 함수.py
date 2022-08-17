import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    zero = [1, 0]
    one = [0, 1]
    c = int(input())
    if c >= 2:
        for i in range(c-1):
            zero.append(one[-1])
            one.append(zero[-2]+one[-1])


    print(zero[c], one[c])


