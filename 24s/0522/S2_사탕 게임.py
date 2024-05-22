'''
3
CCP
CCP
PPC

4
PPPP
CYZY
CCPY
PPCC

5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

'''
# 구현, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

N = int(input())

board = [list(input()) for _ in range(N)]
ans = 0
def check(board):
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        cnt = 1

        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt

for i in range(N):
    for j in range(N):
        if j + 1< N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]


        if i + 1< N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)