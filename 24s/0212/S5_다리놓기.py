'''
3
2 2
1 5
13 29
'''
# DP

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    west = [i for i in range(N)]
    east = [i for i in range(M)]
    dp = [[0] * 30 for _ in range(30)]
    for i in range(30):
        for j in range(30):
            if i == 1:
                dp[i][j] = j

            else:
                if i == j:
                    dp[i][j] = 1

                elif i < j :
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    print(dp[N][M])