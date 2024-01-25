'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''
# R : 1, G : 2, B : 3
import sys
sys.setrecursionlimit(1000000)

N = int(input())
board = [list(map(str, input())) for _ in range(N)]
RGB = 0             # 일반인의 영역 갯수
GB = 0              # 적록색약(R==G)일때의 영역 갯수

visited = [[0] * N for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def DFS(x, y):
    now_color = board[x][y]             # x, y 좌표의 색깔이 현재 찾는 색깔
    visited[x][y] = 1                   # 처음 방문하면 1로 표시
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N :
            if visited[nx][ny] == 0 :           # 방문한 곳이 0일때
                if board[nx][ny] == now_color:          # 현재와 상하좌우 칸의 색이 같다면 DFS를 반복한다.
                    DFS(nx, ny)


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            DFS(i, j)
            RGB += 1


visited = [[0] * N for _ in range(N)]       # 적록색약 일때의 visited 초기화
# 적록색약일때 R = G로 바꿔준다.
for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 :
            DFS(i, j)
            GB += 1

print(RGB ,GB)