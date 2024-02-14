'''
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''
# 그래프이론, 다익스트라, 최단경로

import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
bus = [[] for _ in range(N+1)]
for i in range(M):
    s, e, cost = map(int, input().split())
    bus[s].append((e, cost))

start, end = map(int, input().split())

def dijkstra(graph, start):
    distance = [100000001] * (N+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for next, next_dist in graph[now]:
            temp = dist + next_dist
            if temp < distance[next]:
                distance[next] = temp
                heapq.heappush(queue, [temp, next])

    return distance

answer = dijkstra(bus, start)
print(answer[end])