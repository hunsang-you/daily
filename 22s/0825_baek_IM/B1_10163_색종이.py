# python으로 하면 53점, pypy로 돌리면 100점이 나온다.
import sys
N = int(sys.stdin.readline())

board = [[0] * 1001 for _ in range(1001)]
# paper = [list(map(int, input().split())) for _ in range(T)]


for i in range(N):
    x1, y1, w, h = map(int, input().split())


    for k in range(x1, x1+w):           # 각 사각형의 번호 +1 만큼 (i+1) 그 숫자를 사각형에 채워준다.
        for l in range(y1, y1+h):
            board[k][l] = i + 1


for i in range(N):      # 각 테스트 케이스에 해당하는 숫자의 사각형 갯수를 세어서 출력한다.
    cnt = 0
    for num in board:
        cnt += num.count(i+1)
    print(cnt)
