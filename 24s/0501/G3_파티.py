'''
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90

2 100
10 60 40
50 90 20

8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0

'''
# 그래프 이론, 다익스트라, 최단경로, 다이나믹 프로그래밍

import sys, heapq
input = sys.stdin.readline

N, D = map(int, input().split())

graph = [[] for _ in range(D+1)]
distance = [int(1e9)] * (D+1)
for i in range(D):
    graph[i].append((i+1, 1))

for _ in range(N):
    u, v, d = map(int, input().split())
    if v > D:
        continue
    graph[u].append((v, d))


def dijkstra(s):
    queue = []
    heapq.heappush(queue, (0, s))
    distance[s] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(0)
print(distance[D])