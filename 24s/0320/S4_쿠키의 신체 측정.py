'''
5
_____
__*__
_***_
__*__
_*_*_

10
__________
_____*____
__******__
_____*____
_____*____
_____*____
____*_*___
____*_____
____*_____
____*_____

9
____*____
*********
____*____
____*____
____*____
___*_*___
___*_*___
___*_*___
___*_*___

'''
# 구현

import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(str, input().rstrip())) for _ in range(N)]

# 머리 찾기
def head(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                return i, j

# 왼팔 길이(심장 바로 왼쪽)
def left_hand(x, y):
    cnt = 0
    for i in range(y):
        if board[x+1][i] == '*':
            cnt += 1

    return cnt

# 오른팔 길이(심장 바로 오른쪽)
def right_hand(x, y):
    cnt = 0
    for i in range(N-1, y, -1):
        if board[x+1][i] == '*':
            cnt += 1
    return cnt

# 허리(심장아래, 다리위)
def body(x, y):
    cnt = 0
    for i in range(x+2, N):
        if board[i][y] == '*':
            cnt += 1
    return cnt

# 왼쪽다리(허리아래부터 시작)
def left_leg(x, y):
    cnt = 0
    temp = body(x, y)
    for i in range(x+temp+1, N):
        if board[i][y-1] == '*':
            cnt += 1
    return cnt

# 오른쪽다리(허리 아래부터 시작)
def right_leg(x, y):
    cnt = 0
    temp = body(x, y)
    for i in range(x+temp+1, N):
        if board[i][y+1] == '*':
            cnt += 1
    return cnt

# 심장위치
x, y = head(board)

print(x+2, y+1)
print(left_hand(x, y), end=" ")
print(right_hand(x, y), end=" ")
print(body(x, y), end=" ")
print(left_leg(x, y), end=" ")
print(right_leg(x, y), end=" ")