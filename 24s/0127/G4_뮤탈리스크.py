'''
3
12 10 4

3
54 18 6

1
60

3
1 1 1

2
60 40
'''
# DP, DFS

import sys
input = sys.stdin.readline

N = int(input())
SCV = list(map(int, input().split()))

while len(SCV) < 3:
    SCV.append(0)

dp = [[[0] * 61 for _ in range(61)] for _ in range(61)]


def DFS(x, y, z):
    if x == 0 and y == 0 and z == 0:
        return 0
    if dp[x][y][z] :
        return dp[x][y][z]

    dp[x][y][z] = 1 + min(DFS(max(x-9, 0), max(y-3, 0), max(z-1, 0)), DFS(max(x-9, 0), max(y-1, 0), max(z-3, 0)), DFS(max(x-3, 0), max(y-9, 0), max(z-1, 0)),
                          DFS(max(x-3, 0), max(y-1, 0), max(z-9, 0)), DFS(max(x-1, 0), max(y-3, 0), max(z-9, 0)), DFS(max(x-1, 0), max(y-9, 0), max(z-3, 0)))
    return dp[x][y][z]

print(DFS(SCV[0], SCV[1], SCV[2]))