'''
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

'''
# 그래프이론

import sys
input = sys.stdin.readline

def DFS(depth, cnt):
    check[depth] = 1
    for i in graph[depth]:
        if check[i] == 0:
            cnt = DFS(i, cnt+1)
    return cnt

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    check = [0] * (N+1)
    check[1] = 0
    cnt = DFS(1, 0)
    print(cnt)
