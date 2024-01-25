'''
사각형의 왼쪽아래의 x,y  오른쪽위의 x,y
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''

rect = [list(map(int, input().split())) for _ in range(4)]
board = [[0] * 100 for _ in range(100)]
sumV= 0

for i in range(4):
    x1, y1, x2, y2 = rect[i]                # x y 변수 설정

    for x in range(x1, x2):                 # 입력된 사각형의 면적을 전부 1로 바꿔준다.
        for y in range(y1, y2):
            board[x][y] = 1

for i in range(100):                        # 전체 영역에서의 합을 구한다.
    for j in range(100):
        sumV += board[i][j]


print(sumV)