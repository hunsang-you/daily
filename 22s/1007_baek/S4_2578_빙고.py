'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
def func(lst):
    bingo = 0
    # 가로가 빙고일때
    for i in range(5):
        if sum(lst[i]) == 0:
            bingo += 1
    # 세로가 빙고일때
    for i in range(5):
        tmp = 0
        for j in range(5):
            if lst[j][i] == 0:
                tmp += 1
        if tmp == 5:
            bingo += 1
    # 대각선이 빙고
    tmp1 = []       # 우하단
    tmp2 = []       # 우상단
    for i in range(5):
        tmp1.append(lst[i][i])
        tmp2.append(lst[i][4 - i])
    if sum(tmp1) == 0:
        bingo += 1
    if sum(tmp2) == 0:
        bingo += 1
    return bingo

board = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

cnt = 0

for i in range(5):
    for j in range(5):

        for k in range(5):
            for l in range(5):
                if call[i][j] == board[k][l]:
                    board[k][l] = 0
                    cnt += 1
                if cnt >= 12 :
                    if func(board) >= 3:
                        print(cnt)
                        exit()
