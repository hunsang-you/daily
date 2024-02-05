'''
10
10 -4 3 1 5 6 -35 12 21 -1
'''
# DP

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp = [[i for i in numbers] for _ in range(2)]

for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + numbers[i], dp[0][i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + numbers[i])

print(max(max(dp[0]), max(dp[1])))