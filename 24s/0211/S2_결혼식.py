'''
6
5
1 2
1 3
3 4
2 3
4 5

6
5
2 3
3 4
4 5
5 6
2 5
'''
# 그래프

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(x):
    queue = deque([x])
    visited[x] = 1

    while queue:
        number = queue.popleft()

        for friend in graph[number]:
            if visited[friend] == 0:
                queue.append(friend)
                visited[friend] = visited[number] + 1

BFS(1)

answer = 0


for i in range(1, N+1):
    if 0 < visited[i] <= 3:
        answer += 1

print(answer-1)