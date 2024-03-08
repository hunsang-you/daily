'''
5 3
-1 1 2 3 4
2 2
3 4
5 6

'''
# 다이나믹 프로그래밍, 그래프이론, 탐색, 트리, DFS, 트리에서의 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

people = list(map(int, input().split()))
comp = [0] * (N+1)
answer = [0] * (N+1)

for i in range(1, N):
    comp[i+1] = people[i]

for _ in range(1, M+1):
    i, w = map(int, input().split())

    answer[i] += w

for i in range(2, N+1):
    answer[i] += answer[comp[i]]

for i in range(1, N+1):
    print(answer[i], end=" ")