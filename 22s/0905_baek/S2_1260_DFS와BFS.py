'''
4 5 1
1 2
1 3
1 4
2 4
3 4
=======
5 5 3
5 4
5 2
1 2
3 4
3 1
'''
from collections import deque
N, M, V = map(int, input().split())
graph = [[] * N for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):                 # 방문한 정점이 여러 개인 경우, 작은 것부터 방문하므로 정렬을 해준다.
    graph[i].sort()

visited = [0] * (N+1)


def DFS(V):
    print(V, end=' ')
    visited[V] = 1                  # 방문한 곳을 1로 바꾸고 그렇지 않은 곳이라면 재귀를 돌리고 1로 바꾼다.
    for i in graph[V]:
        if not visited[i]:
            DFS(i)
            visited[i] = 1


def BFS(V):
    queue = deque([V])
    visited[V] = 1
    while queue :
        lst = queue.popleft()
        print(lst, end=' ')
        for i in graph[lst]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

DFS(V)
visited = [0] * (N+1)               # BFS를 실행하기위해 visited를 초기화
print()
BFS(V)


# print(DFS(V))
# print(BFS(V))


# print(graph)