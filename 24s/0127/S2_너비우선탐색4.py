'''
5 5 1
1 4
1 2
2 3
2 4
3 4
'''
# BFS


import sys
input = sys.stdin.readline
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1] * (N+1)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def BFS(s):
    queue = deque([(s, 1)])
    visited[s] = 1
    t = 2
    answer = 0
    while queue:
        now, dep = queue.popleft()

        for i in sorted(graph[now]):
            if visited[i] == -1:
                visited[i] = dep * t
                answer += visited[i]
                t += 1
                queue.append((i, dep+1))

    return answer

result = BFS(R)
print(result)