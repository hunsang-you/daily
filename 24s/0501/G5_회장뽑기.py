'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

'''
# 그래프 이론, 탐색, BFS, 최단경로, 플로이드-워셜

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1:
        break
    graph[u].append(v)
    graph[v].append(u)

def BFS(n):
    queue = deque()
    queue.append(n)
    visited = [-1] * (N+1)
    visited[n] = 0

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                queue.append(i)
    return max(visited)

score = 50
ans = []

for i in range(1, N+1):
    temp = BFS(i)

    if temp < score:
        score = temp
        ans = [i]

    elif temp == score:
        ans.append(i)

print(score, len(ans))
print(*ans)