'''
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
'''
import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
zero = []
def rowcheck(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True


def colcheck(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

def reccheck(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[nr+i][nc+j] == num:
                return False
    return True

def sdoku(dep):
    if dep == len(zero):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end="")
            print()
        exit()

    nr, nc = zero[dep]

    for num in range(1, 10):
        if rowcheck(nr, num) and colcheck(nc, num) and reccheck(nr, nc, num):
            board[nr][nc] = num
            sdoku(dep+1)
            board[nr][nc] = 0


for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            zero.append((r, c))

sdoku(0)