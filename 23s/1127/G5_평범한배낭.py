'''
4 7
6 13
4 8
3 6
5 12
'''
# DP

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0,0]]
DP = [[0] * (K+1) for _ in range(N+1)]
for i in range(N):
    stuff.append(list(map(int, input().split())))

stuff.sort()

for i in range(1, N+1):
    for j in range(1, K+1):
        W = stuff[i][0]
        V = stuff[i][1]

        if j < W :
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W]+V)

print(DP[N][K])
