a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())

def GCD(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    return gcd

b3 = b1*b2
a3 = a1*b2 + a2*b1

g = GCD(a3,b3)
print(a3//g, b3//g)