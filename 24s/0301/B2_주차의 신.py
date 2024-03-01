'''
2
4
24 13 89 37
6
7 30 41 14 39 42

'''
# 수학, 구현

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    market = list(map(int, input().split()))
    market.sort()

    answer = 0
    for i in range(1, N):
        answer += (market[i] - market[i-1]) * 2
    print(answer)