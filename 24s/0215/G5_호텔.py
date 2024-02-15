'''
12 2
3 5
1 1

10 3
3 1
2 2
1 3

10 10
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10

100 6
4 9
9 11
3 4
8 7
1 2
9 8
'''
# DP

import sys
input = sys.stdin.readline

C, N = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dp = [1e9 for _ in range(C+100)]
dp[0] = 0

for cost, people in data:
    for i in range(people, C+100):
        dp[i] = min(dp[i-people]+cost, dp[i])

print(min(dp[C:]))