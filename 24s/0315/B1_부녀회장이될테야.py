'''
2
1
3
2
3

'''
# 수학, 구현, 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층
    DP = [0] + [x for x in range(1, n+1)]
    # 층수 만큼
    for i in range(1, k+1):
        for j in range(1, n+1):
            DP[j] += DP[j-1]

    print(DP[n])