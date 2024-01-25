'''
3 3
1 1 0
1 1 1
1 0 1
1 1 1
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''
dx = [-1, 0, 1, 0]  # 북0 동1 남2 서3
dy = [0, 1, 0, -1]
# (북->서) = (0-3), (서->남) = (3-2), (남->동) = (2-1), (동->북) = (1-0)
# (0+3)%4           (3+3)%4             (2+3)%4         (1+3)%4  으로 방향이 바뀜
# 0123북동남서 -> 3210서남동북


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]       # 청소했는지 확인

# 시작지점을 청소
visited[r][c] = 1
cnt = 1

while True:
    clear = 0               # 청소시도
    for k in range(4):
        d = (d+3) % 4       # 왼쪽방향으로 돌린다.
        nx = r + dx[d]
        ny = c + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == 1 : continue   # 경계조건
        if visited[nx][ny] == 0:        # 청소하지 않은 곳 방문
            visited[nx][ny] = 1
            cnt += 1
            r = nx
            c = ny
            clear = 1       # 청소완료
            break

    if clear == 0 :     # 네방향에 대해 청소가 안될때
        if board[r-dx[d]][c-dy[d]] == 1:    # 뒤로 후진했는데도 청소가 불가능하면
            print(cnt)
            break

        else:       # 후진했는데 청소가 된다면 좌표변경
            r = r - dx[d]
            c = c - dy[d]



