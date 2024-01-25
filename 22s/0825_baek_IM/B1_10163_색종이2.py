import sys
N = int(input())

board = [[0] * 1001 for _ in range(1001)]
# paper = [list(map(int, input().split())) for _ in range(T)]


for i in range(1, N+1):
    x1, y1, w, h = map(int, input().split())


    for k in range(x1, x1+w):           # 각 사각형의 번호 +1 만큼 (i+1) 그 숫자를 사각형에 채워준다.
        for l in range(y1, y1+h):
            board[k][l] = i


cnt = [0] * (N+1)

for i in range(1001):
    for j in range(1001):
        if board[i][j] :
            cnt[board[i][j]] += 1

for i in range(1, N+1):
    print(cnt[i])