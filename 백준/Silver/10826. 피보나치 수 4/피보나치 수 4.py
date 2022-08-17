import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

if n >=2:
    for i in range(n):
        dp.append(dp[-2]+dp[-1])

print(dp[n])