'''
3
0 0 0
0 0 0
0 9 0

3
0 0 1
0 0 0
0 9 0

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

'''
# 구현, 그래프 이론, 탐색, 시뮬레이션, BFS

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

shark_size = 2

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x, y = 0, 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:    # 상어의 위치
            x, y = i, j         # 좌표 저장
            board[i][j] = 0     # 상어가 있던 자리 0으로

ans = cnt = 0
def BFS(x, y):
    global shark_size
    visited = [[0] * N for _ in range(N)]
    tlst = []
    eat = 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        # eat == visited[i][j]      # eat에 적힌 거리는 모두 리스트에 넣었음(방문했음)
        if eat == visited[i][j]:
            return tlst, eat-1

        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and board[ni][nj] <= shark_size:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                # 나보다 작은 물고기인 경우 먹을 리스트에 추가
                if shark_size > board[ni][nj] > 0:
                    tlst.append((ni, nj))
                    eat = visited[ni][nj]

    # 먹을수 없는 물고기가 없는 경우(방문이 모두 끝남)
    return tlst, eat - 1


while True:
    tlst, dist = BFS(x, y)
    if len(tlst) == 0:      # 더이상 먹을 물고기가 없는 경우
        break
    tlst.sort(key=lambda x:(x[0], x[1]))
    x, y = tlst[0]          # 이동한 위치로 좌표 변경
    board[x][y] = 0         # 먹었으니 0
    cnt += 1
    if shark_size == cnt:       # 크기만큼 물고기 먹은경우 크기 증가
        shark_size += 1
        cnt = 0
    ans += dist

print(ans)