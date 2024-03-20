'''
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

3 3 1 1 9
1 2 3
4 0 5
6 7 8
1 3 2 2 4 4 1 1 3

2 2 0 0 16
0 2
3 4
4 4 4 4 1 1 1 1 3 3 3 3 2 2 2 2

3 3 0 0 16
0 1 2
3 4 5
6 7 8
4 4 1 1 3 3 2 2 4 4 1 1 3 3 2 2



'''
# 구현, 시뮬레이션

import sys
input = sys.stdin.readline

# 지도의 크기 N X M 주사위의 좌표 x, y 명령의 개수 K
N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
command = list(map(int, input().split()))

# 초기 주사위면
n1=n2=n3=n4=n5=n6=0

# 동서북남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

ans_lst = []
# 명령방향대로 이동 후 처리
for dr in command:
    # 이동 후 범위 내 라면 처리
    nx = x + dx[dr]
    ny = y + dy[dr]

    if 0 <= nx < N and 0 <= ny < M:
        # 주사위 면 굴리기
        if dr == 1:     # 동쪽이면
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif dr == 2:   # 서쪽이면
            n1, n3, n4, n6 = n3, n6, n1, n4

        elif dr == 3:   # 북쪽이면
            n1, n2, n5, n6 = n5, n1, n6, n2

        else:       # 남쪽이면
            n1, n2, n5, n6 = n2, n6, n1, n5

        # 이동한 바닥판이 0인지 아닌지에 따라 처리
        if board[nx][ny] == 0:
            board[nx][ny] = n6
        else:
            n6, board[nx][ny] = board[nx][ny], 0

        ans_lst.append(n1)      # 윗면 값 추가
        x, y = nx, ny       # 다음 이동 처리

print(*ans_lst, sep="\n")