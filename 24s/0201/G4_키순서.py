'''
6 6
1 5
3 4
5 4
4 2
4 6
5 2

6 7
1 3
1 5
3 4
5 4
4 2
4 6
5 2

6 3
1 2
2 3
4 5
'''
# DFS 최단경로 플로이드-워셜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [([0] * N) for _ in range(N+1)]
result = 0
for i in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(N):
    temp = 0
    for j in range(N):
        temp += graph[i][j] + graph[j][i]

    if temp == (N-1):
        result += 1

print(result)