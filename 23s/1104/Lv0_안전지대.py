'''
board	                                                                                                                   result
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	                                    16
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	                                    13
[[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0
'''

from collections import deque


def solution(board):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    L = len(board)
    visited = [[0] * L for _ in range(L)]

    def BFS(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            a, b = queue.popleft()
            visited[a][b] = 1

            for k in range(8):
                nx = dx[k] + a
                ny = dy[k] + b

                if 0 <= nx < L and 0 <= ny < L and visited[nx][ny] == 0:
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
                    else:
                        board[nx][ny] = -1

    for i in range(L):
        for j in range(L):
            if board[i][j] == 1:
                BFS(i, j)

    answer = 0
    for i in range(L):
        answer += board[i].count(0)

    return answer