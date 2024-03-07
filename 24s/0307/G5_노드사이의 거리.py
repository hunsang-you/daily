'''
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2

'''
# 그래프이론, 탐색, BFS, DFS, 트리

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
node = []


for _ in range(N-1):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))
    graph[v].append((u, d))


def BFS(start, target):
    queue = deque()
    queue.append((start, 0))
    visited = [0] * (N+1)
    visited[start] = 1

    while queue:
        now, dist = queue.popleft()

        # 찾는 노드와 번호가 일치할 때 거리 리턴
        if now == target:
            return dist

        for i, d in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append((i, dist+d))


for _ in range(M):
    node1, node2 = map(int, input().split())
    print(BFS(node1, node2))
