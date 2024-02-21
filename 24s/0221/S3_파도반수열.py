'''
2
6
12
'''
# DP

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    DP = [0] * (101)

    DP[1] = 1
    DP[2] = 1
    DP[3] = 1
    DP[4] = 2
    DP[5] = 2
    DP[6] = 3


    for i in range(3, N+1):
        DP[i] = DP[i-3] + DP[i-2]


    print(DP[N])