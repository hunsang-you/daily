'''
4
1 5 6 7

5
10 9 8 7 6

10
1 1 2 3 5 8 13 21 34 55

10
5 10 11 12 13 30 35 40 45 47

4
5 2 8 10

4
3 5 15 16

'''
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))

DP = [0 for _ in range(N+1)]

for i in range(N+1):
    for j in range(1, i+1):
        DP[i] = max(DP[i], DP[i-j] + P[j])

print(max(DP))