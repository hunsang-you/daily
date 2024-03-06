'''
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32

'''
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    DP = [[0] * (K+1) for _ in range(K+1)]

    for i in range(1, K+1):
        for j in range(1, K+1):
            if j == i + 1:
                DP[i][j] = arr[i] + arr[j]

    for i in range(K-1, 0 , -1):
        for j in range(1, K+1):
            if DP[i][j] == 0 and j > i:
                DP[i][j] = min([DP[i][k] + DP[k+1][j] for k in range(i, j)]) + sum(arr[i:j+1])

    print(DP[1][K])
