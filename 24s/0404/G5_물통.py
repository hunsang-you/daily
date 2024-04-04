'''
8 9 10

'''
# 그래프 이론, 탐색, BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

A, B, C = map(int, input().split())

queue = deque()
# A와 B에 담긴 현재 물
queue.append((0, 0))

visited = [[0] * (B+1) for _ in range(A+1)]
visited[0][0] = 1
ans = []

def pour(x, y):
    if visited[x][y] == 0:
        visited[x][y] = 1
        queue.append((x, y))

def BFS():
    while queue:
        # A-x B-y C-z
        x, y = queue.popleft()
        z = C - x - y

        # A가 비어있으면 C를 리스트에 저장
        if x == 0:
            ans.append(z)


        # A에서 B로 물 이동
        water = min(x, B - y)
        pour(x - water, y + water)
        # A에서 C로 이동
        water = min(x, C - z)
        pour(x - water, y)

        # B에서 A로 이동
        water = min(y, A - x)
        pour(x + water, y - water)
        # B에서 C로 이동
        water = min(y, C - z)
        pour(x, y - water)

        # C에서 A로 이동
        water = min(z, A - x)
        pour(x + water, y)
        # C에서 B로 이동
        water = min(z, B - y)
        pour(x, y + water)

BFS()
ans.sort()
print(*ans)