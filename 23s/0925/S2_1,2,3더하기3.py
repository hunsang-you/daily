'''
3
4
7
10
'''
import sys
input = sys.stdin.readline
dp = [0 for i in range(1000001)]
T = int(input())
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, 1000001):
    dp[i] = dp[i-3] % 1000000009 + dp[i-2] % 1000000009 + dp[i-1] % 1000000009

for i in range(T):
    N = int(input())
    print(dp[N]%1000000009)

