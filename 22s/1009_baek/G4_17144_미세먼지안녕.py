'''
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1초마다 퍼지는 먼지
def dust():
    new = [[0] * C for _ in range(R)]       # 먼지가 퍼진 새로운 board
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0 :        # 먼지가 존재한다면
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < R and 0 <= ny < C :        # 경계조건
                        if board[nx][ny] != -1:         # 움직이는 칸이 청정기가 아닌 곳에서만
                            new[nx][ny] += board[i][j] // 5      # 새로운칸의 먼지는 기존칸의 //5이고 기존칸은 그만큼 줄어든다
                            tmp += board[i][j] // 5     # 사방으로 빠진 미세먼지
                board[i][j] -= tmp       # 1칸당 빠지는 먼지의 양 * 4칸만큼 줄어듬

    for i in range(R):
        for j in range(C):
            board[i][j] += new[i][j]


def condition():
    pass


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

air_top = 0
air_bot = 0
# 공기 청정기의 위치파악
for i in range(R):
    if board[i][0] == -1:
        air_top = i
        air_bot = i+1

for _ in range(T):
    dust()


# dust()
for i in board:
    print(*i)