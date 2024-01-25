'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''
# 그래프이론, 다익스트라, 최단경로
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

INF = sys.maxsize
dp = [INF] * (V+1)
heap = []

def Dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dp[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if dp[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


Dijkstra(K)
for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])