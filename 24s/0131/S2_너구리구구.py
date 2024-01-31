'''
4
1 2 3
2 3 2
2 4 4
'''
# BFS

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
adj = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

result = 0

for i in range(N-1):
    A, B, C = map(int, input().split())
    adj[A][B] = C
    adj[B][A] = C

def BFS(s):
    global result
    queue = deque()
    queue.append((s, 0))

    while queue:
        v, wei = queue.popleft()
        visited[v] = True
        result = max(result, wei)

        for i in range(1, N+1):
            if visited[i] == False:
                if adj[v][i] != 0:
                    queue.append((i, wei + adj[v][i]))

BFS(1)

print(result)