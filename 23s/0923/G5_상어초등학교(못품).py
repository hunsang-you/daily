'''
3
4 2 5 1 7
3 1 9 4 5
9 8 1 2 3
8 1 9 3 4
7 2 3 4 8
1 9 2 5 7
6 5 2 3 4
5 1 9 2 8
2 9 3 1 4

3
4 2 5 1 7
2 1 9 4 5
5 8 1 4 3
1 2 9 3 4
7 2 3 4 8
9 8 4 5 7
6 5 2 3 4
8 4 9 2 1
3 9 2 1 4
'''
import sys
input = sys.stdin.readline

# |r1-r2| + |c1-c2| = 1 을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.
# 1. 비어있는 칸 중, 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 정한다.
# 2. 1을 만족하는 칸이 여러개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 정한다.
# 3. 2를 만족하는 칸도 여러개인 경우, 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

N = int(input())

student = [list(map(int, input().split())) for _ in range(N*N)]

desk = [[0] * (N+1)for _ in range(N+1)]

# 상 하 좌 우
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for x in range(N*N):

    # 현재 학생
    now = student[x][0]
    like = student[x][1:]
    result = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            if desk[i][j] == 0 :    # 빈자리라면
                like_cnt = 0 # 인접한 칸의 좋아하는 학생수
                empty_cnt = 0 # 인접한 칸의 비어있는 칸 수

                # 각 위치에서 상하좌우 탐색
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (1 <= nx < N+1) and (1 <= ny < N+1):
                        # 인접칸에 좋아하는 학생이 있으면 카운트
                        if desk[nx][ny] in like :
                            like_cnt += 1

                        # 인접칸이 비어있다면 카운트
                        if desk[nx][ny] == 0:
                            empty_cnt += 1

                # 현재의 중심 좌석을 현재 학생을 앉힐 수 있는 자리 후보군에 추가
                result.append((like_cnt, empty_cnt, i, j))

    result = sorted(result, key= lambda x : (-x[0], -x[1], x[2], x[3]))

    # 최적의 자리에 현재 학생 앉히기
    desk[result[0][2]][result[0][3]] = now

# 학생의 번호 별 좋아하는 학생의 번호를 저장할 리스트를 학생의 번호를 기준으로 오름차순 정렬

