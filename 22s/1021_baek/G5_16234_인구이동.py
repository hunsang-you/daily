'''
2 20 50
50 30
20 40
2 40 50
50 30
20 40
2 20 50
50 30
30 40
'''
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
from collections import deque
def func(i, j):
    queue = deque()
    queue.append((i, j))
    union = []          # 연합이 된 국가좌표
    union.append((i, j))
    population = 0              # 각 좌표의 인구
    population += board[i][j]
    visited[i][j] = 1
    while queue :
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(board[x][y] - board[nx][ny]) <= R :         # L ~ R 사이
                    queue.append((nx, ny))
                    union.append((nx, ny))              # 연합좌표에 추가
                    visited[nx][ny] = 1
                    population += board[nx][ny]         # 연합인구 더하기

    new_pop = population // len(union)

    for x, y in union:
        board[x][y] = new_pop


    if len(union) > 1 :     # 자기 자신을 제외하고 연합이 없는것은 뺴고 리턴
        return 1    #union
    else :
        return 0

N, L, R = map(int, input().split())
board = [[0] for _ in range(N)]
for i in range(N):          # 인구값 대입
    board[i] = list(map(int, input().split()))

result = 0
while True:
    cnt = 0
    visited = [[0] * N for _ in range(N)]       # 계속 초기화
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 :
                # print(func(i, j))
                cnt += func(i, j)

    if not cnt:
        break
    result += 1

print(result)






