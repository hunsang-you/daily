'''
3
2 2 2
4 4 4
8 8 8
'''
# 구현, 브루트포스, 시뮬레이션, 백트래킹

import sys
input = sys.stdin.readline
import copy
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
ans = 0


# 왼쪽으로 움직일때
def move_left(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:       #  0이면 그냥 옮김
                    board[i][pointer] = temp

                elif board[i][pointer] == temp:
                    board[i][pointer] *= 2      # temp와 같다면 합쳐져서 옮겨짐
                    pointer += 1                # pointer 변화

                else:               # 0이 아닌 temp와 다른 숫자라면
                    pointer += 1
                    board[i][pointer] = temp        # 그냥 옆에 붙임

    return board

# 오른쪽으로 움직일때
def move_right(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-1, -1, -1):
            if board[i][j] != 0:
                temp = board[i][j]
                board[i][j] = 0

                if board[i][pointer] == 0:
                    board[i][pointer] = temp

                elif board[i][pointer] == temp:
                    board[i][pointer] *= 2
                    pointer -= 1

                else:
                    pointer -= 1
                    board[i][pointer] = temp
    return board


# 아래로 움직일때
def move_up(board):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if board[j][i] != 0:
                temp = board[j][i]
                board[j][i] = 0

                if board[pointer][i] == 0:
                    board[pointer][i] = temp

                elif board[pointer][i] == temp:
                    board[pointer][i] *= 2
                    pointer += 1

                else:
                    pointer += 1
                    board[pointer][i] = temp
    return board

def move_down(board):
    for i in range(N):
        pointer = N-1
        for j in range(N-1, -1, -1):
            if board[j][i] != 0:
                temp = board[j][i]
                board[j][i] = 0

                if board[pointer][i] == 0:
                    board[pointer][i] = temp

                elif board[pointer][i] == temp:
                    board[pointer][i] *= 2
                    pointer -= 1

                else :
                    pointer -= 1
                    board[pointer][i] = temp

    return board


def DFS(n, arr):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(4):
        temp_arr = copy.deepcopy(arr)
        if i == 0:
            DFS(n+1, move_up(temp_arr))

        elif i == 1:
            DFS(n+1, move_down(temp_arr))

        elif i == 2:
            DFS(n+1, move_left(temp_arr))

        else:
            DFS(n+1, move_right(temp_arr))

DFS(0, board)

print(ans)