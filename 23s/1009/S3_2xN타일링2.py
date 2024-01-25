'''
2

8

12
'''
# DP
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())

# n = 1 > 1   n=2 > 3   n=3 > 5   n=4 > 11
# dp[n] = dp[n-2] * 2 + dp[n-1]

dp = [0] * 1001
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[N] % 10007)