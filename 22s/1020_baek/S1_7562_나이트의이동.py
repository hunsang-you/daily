'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]       # 1시 방향부터 시계방향으로
from collections import deque

def func(i, j):       # 시작 좌표 , 도착 좌표
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        if x == x2 and y == y2:     # pop을 했는데 도착 좌표와 같다면 그 좌표값을 return
            return board[x][y]

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            # 경계조건 + 한번 지나간 칸은 다시 지나갈 필요가 없다
            if 0 <= nx < L and 0 <= ny < L and visited[nx][ny] == 0 and board[nx][ny] == 0:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1     # 다음칸을 갈때마다 + 1씩
                visited[nx][ny] = 1




T = int(input())
for tc in range(T):
    L = int(input())
    board = [[0] * L for _ in range(L)]
    visited = [[0] * L for _ in range(L)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    print(func(x1, y1))

    # for i in board:
    #     print(*i)