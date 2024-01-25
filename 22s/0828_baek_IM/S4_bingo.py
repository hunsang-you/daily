'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
----
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''
# 5 X 5 빙고판
board = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]       # 빙고판에 불린 숫자를 0에서 1로 표시해 주는 리스트



bingo = 0
for i in range(5):
    for j in range(5):
        while bingo < 3 :
            for k in range(5):
                for l in range(5):
                    if board[k][l] == ans[i][j] :
                        visited[k][l] = 1
                        # if