'''
4 2 1
1 1 5 2 2
1 4 7 1 6

4 2 2
1 1 5 2 2
1 4 7 1 6

4 2 3
1 1 5 2 2
1 4 7 1 6

7 5 3
1 3 5 2 4
2 3 5 2 6
5 2 9 1 7
6 2 1 3 5
4 4 2 4 2

'''
# 구현, 시뮬레이션
# 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

fireballs = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    # [0]:r, [1]:c, [2]:질량, [3]:속도, [4]:방향
    # 개체별 이동
    for i in range(len(fireballs)):
        fireballs[i][0] = (fireballs[i][0] + dx[fireballs[i][4]] * fireballs[i][3]) % N + 1
        fireballs[i][1] = (fireballs[i][1] + dy[fireballs[i][4]] * fireballs[i][3]) % N + 1

    # 전체개체 정렬(좌표기준으로 정렬 -> 같은 좌표 처리(
    fireballs.sort(key=lambda x:(x[0], x[1]))
    fireballs.append([100, 100, 0, 0, 0])       # 패딩 마지막요소

    new = []

    # 2개 이상일 때 같은 좌표 합치고 나누고 new에 추가
    i = 0
    while i < len(fireballs) - 1:
        # 기준좌표
        si, sj, m, s, d = fireballs[i]
        start = 0           # 같으면 0, 2, 4, 8
        for j in range(i+1, len(fireballs)):
            # 같은 좌표라면
            if (si, sj) == (fireballs[j][0], fireballs[j][1]):
                m += fireballs[j][2]
                s += fireballs[j][3]
                if d % 2 != fireballs[j][4] % 2 :         # 다른방향 start = 1
                    start = 1
            else:           # 다른 좌표라면
                if j-i == 1:        # 1개 -> 그냥추가
                    new.append(fireballs[i])

                else:       # 여러개
                    if m // 5 > 0 :         # 나눠도 1 이상이면
                        for dr in range(start, start+8, 2):
                            new.append([si, sj, m//5, s//(j-i), dr])
                break
        i = j
    fireballs = new
ans = 0
for lst in fireballs:
    ans += lst[2]
print(ans)