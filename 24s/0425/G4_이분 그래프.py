'''
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

'''
# 그래프 이론, 탐색, BFS, DFS, 이분그래프

import sys
input = sys.stdin.readline
from collections import deque

K = int(input())

def BFS(start, group):
    queue = deque([start])
    visited[start] = group

    while queue:
        x = queue.popleft()

        for i in graph[x]:      # 정점 x에서 연결되어있는 다른 정점들 i
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] * (-1)      # x와 연결된 i를 x와 구분짓는다
            elif visited[i] == visited[x]:      # 만약 서로 연결된 두 정점의 v가 같다면 이분그래프가 아니다.
                return False

    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    check = True
    for i in range(1, V+1):
        if visited[i] == 0:
            check = BFS(i, 1)
            if check == False:
                break

    if check == True:
        print("YES")

    else:
        print("NO")