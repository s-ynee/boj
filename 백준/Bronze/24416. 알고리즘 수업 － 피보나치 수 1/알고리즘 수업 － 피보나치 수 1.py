import sys
input = sys.stdin.readline()

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    cnt2 = 0
    for i in range(3, n + 1):
        cnt2 += 1
        dp[i] = dp[i - 1] + dp[i - 2]
    return cnt2


n = int(input)

print(fib1(n),fib2(n))