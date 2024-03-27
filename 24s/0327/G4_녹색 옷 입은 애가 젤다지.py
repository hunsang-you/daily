'''
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0

'''
# 다익스트라, 최단경로, 그래프 이론

import sys, heapq
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, board[0][0]))
    distance[0][0] = 0

    while queue:
        x, y, dist = heapq.heappop(queue)
        if x == N-1 and y == N-1:
            print(f'Problem {case}: {distance[x][y]}')
            break

        else:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    new_dist = dist + board[nx][ny]

                    if new_dist < distance[nx][ny]:
                        distance[nx][ny] = new_dist
                        heapq.heappush(queue, (nx, ny, new_dist))

case = 1
while True:
    N = int(input())

    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[1e9] * N for _ in range(N)]

    dijkstra()

    case += 1