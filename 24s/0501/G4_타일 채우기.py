'''
2

'''
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())

DP = [0 for _ in range(31)]

DP[2] = 3

for i in range(4, N+1, 2):
    DP[i] = DP[i-2] * 3 + sum(DP[:i-2]) * 2 + 2

print(DP[N])