'''
5 5 1
1 4
1 2
2 3
2 4
3 4
'''

import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
visited[R] = cnt

def BFS():
    global cnt
    queue = deque()
    queue.append(R)
    while queue:
        node = queue.popleft()
        graph[node].sort(reverse=True)
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                cnt += 1
                visited[i] = cnt


for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

BFS()

for i in visited[1:]:
    print(i)
