'''
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

'''
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

DP = [1] * N

line.sort()

for i in range(1, N):
    for j in range(i):
        if line[j][1] < line[i][1]:
            DP[i] = max(DP[i], DP[j] + 1)

print(N - max(DP))
