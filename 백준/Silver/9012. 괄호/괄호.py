import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    s = input()
    s = s[:-1]
    cnt_r = 0
    cnt_l = 0
    out ="YES"
    state = True
    # while state == True:
    for j in s:
        if j == "(" and cnt_r >= cnt_l:
            cnt_r += 1
            pass
        elif j == ")" and cnt_r >= cnt_l:
            cnt_l += 1
            pass

        else:
            out = "NO"
            state = False
            break


    if cnt_r != cnt_l:
        out = "NO"
    print(out)
