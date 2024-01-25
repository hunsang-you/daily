'''
5 4
0 1
1 2
2 3
3 4

5 5
0 1
1 2
2 3
3 0
1 4

6 5
0 1
0 2
0 3
0 4
0 5

8 8
1 7
3 7
4 7
3 4
4 6
3 5
0 4
2 7
'''
# DFS, 백트래킹
# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [0] * 2001
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def DFS(idx, depth):
    global ans
    visited[idx] = 1

    if depth == 4:
        ans = 1
        return

    for i in graph[idx]:
        if visited[i] == 0:
            visited[i] = 1
            DFS(i, depth+1)
            visited[i] = 0

for i in range(N):
    DFS(i, 0)
    visited[i] = 0
    if ans :
        break

if ans:
    print(1)

else:
    print(0)

