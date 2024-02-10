'''
5 3

11 3
'''
# DP

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[] for _ in range(N)]

for i in range(N):
    for j in range(i+1):
        if i == 0 or j == 0 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])

print(dp[N-1][K-1])