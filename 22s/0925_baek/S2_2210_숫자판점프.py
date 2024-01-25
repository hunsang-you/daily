'''
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1
'''
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def DFS(x, y, num):
    if len(num) == 6 :
        if num not in result :
            result.append(num)
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5 :
            DFS(nx, ny, num + board[nx][ny])


board = [list(map(str, input().split())) for _ in range(5)]
result = []

for i in range(5):
    for j in range(5):
        DFS(i, j, board[i][j])

print(len(result))
