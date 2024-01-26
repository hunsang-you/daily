'''
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

4 9
8 52
6 80
26 42
2 72
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21
'''
# BFS

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [0] * 101
visited = [0] * 101

ladder = dict()
snake = dict()

for i in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for i in range(M):
    u, v = map(int, input().split())
    snake[u] = v

queue = deque([1])
visited[1] = True

while queue:
    now = queue.popleft()
    for i in range(1, 7):
        move = now + i

        if 0 < move <= 100 and visited[move] == 0:
            if move in ladder.keys():
                move = ladder[move]

            if move in snake.keys():
                move = snake[move]

            if visited[move] == 0:
                queue.append(move)
                visited[move] = True
                board[move] = board[now] + 1

print(board[-1])