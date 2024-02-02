'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
'''
# 다익스트라 최단경로
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = 1e9
for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (N+1)
    distance[start] = 0
    hq = [(0, start)]

    while hq:
        cost, node = heapq.heappop(hq)

        for next, val in graph[node]:
            if distance[next] > distance[node] + val:
                distance[next] = distance[node] + val
                heapq.heappush(hq, (distance[next], next))

    return distance[end]

# 1 -> v1 -> v2 -> N
path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
# 1 -> v2 -> v1 -> N
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= INF and path2 >= INF:
    print(-1)

else:
    print(min(path1, path2))