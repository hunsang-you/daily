'''
7 7
1 2
2 3
2 4
3 4
1 5
5 7
6 7
3
4 3 5

7 7
1 2
2 3
2 4
3 4
1 5
5 7
6 7
2
3 5

2 1
1 2
1
1


100000 1
4 3
5
3 4 5 6 100000
'''
# 그래프 이론,탐색, BFS, DFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# 클럽 곰곰이가 존재하는 정점의 개수 S
S = int(input())

# 팬클럽이 존재하는 정점의 번호
position = list(map(int, input().split()))


def BFS(n):
    queue = deque()
    queue.append(n)
    visited = [0] * (N+1)       # 방문 여부
    visited[n] = 1

    while queue:
        now = queue.popleft()   # 현재 있는 정점

        for next in graph[now]:  # 현재 정점과 연결된 정점들
            if visited[next] == 0:
                if next in position:
                    visited[next] = 2

                else:
                    visited[next] = 1
                queue.append(next)

    # 다음 정점이 없고, visited == 2인 곳은 가는동안 팬클럽이 있던 것
    for i in range(1, len(graph)):
        if len(graph[i]) == 0 and visited[i] == 2:
            return 'Yes'

        elif len(graph[i]) == 0 and visited[i] == 1:
            return 'yes'

if 1 in position:
    print('Yes')
else:
    print(BFS(1))
