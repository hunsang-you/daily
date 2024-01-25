'''
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
'''
# 그래프이론, 너비우선탐색, 다익스트라, 최단경로

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [0] * (N+1)
visited = [0] * (N+1)

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)


def BFS(start):
    answer = []
    queue = deque([start])
    visited[start] = 1
    distance[start] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

BFS(X)