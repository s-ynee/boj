import sys
input = sys.stdin.readline

n = int(input())
pack = -1

if n%5 == 0:
    pack = n//5
    if n == 0:
        pack = -1
elif n%5 == 1 and n >= 6:
    pack = (n//5-1) + (n-(n//5-1)*5)//3
elif n%5 == 2 and n >= 12:
    pack = (n//5-2) + (n-(n//5-2)*5)//3
elif n%5 == 3 :
    pack = (n//5-1) + (n-(n//5-1)*5)//3
    if n == 3:
        pack == 1
elif n%5 == 4 and n >= 9:
    pack = (n//5-1) + (n-(n//5-1)*5)//3




print(pack)


