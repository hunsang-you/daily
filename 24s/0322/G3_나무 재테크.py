'''
1 1 4
1
1 1 1

1 1 4
1
1 1 1

5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 3
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 4
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 5
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 6
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

'''
# 구현, 자료구조, 시뮬레이션

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N, M, K = map(int, input().split())

arr = [[5] * N for _ in range(N)]               # 초기양분 5
add_arr = [list(map(int, input().split())) for _ in range(N)]      # 겨울 추가양분
v = [[[] for _ in range(N)] for _ in range(N)]


for _ in range(M):
    i, j, age = map(int, input().split())
    v[i-1][j-1].append(age)


for _ in range(K):  # K년 반복
    # 봄 + 여름 : 나이순으로 처리 -> 양분부족시 나무 죽고 ==> 1//2 추가
    for i in range(N):
        for j in range(N):
            v[i][j].sort()              # 나무가 어린순으로 오름차순 정렬
            for k in range(len(v[i][j])):           # 어린 나무 순서대로 처리
                if v[i][j][k] <= arr[i][j]:         # 나이보다 양분이 많으면
                    arr[i][j] -= v[i][j][k]         # 나이만큼 양분뻄
                    v[i][j][k] += 1                 # 나이 1살 증가

                else:                       # 양분이 나이보다 적다면
                    while k < len(v[i][j]):     # 나머지 나무는 양분
                        arr[i][j] += (v[i][j].pop() // 2)
                    break


    # 가을 : 나이가 5의 배수인 경우 인접 8칸에 나무 1 생성
    for i in range(N):
        for j in range(N):
            for k in range(len(v[i][j])):       # 현 위치의 모든 나무 처리
                if v[i][j][k] % 5 == 0:         # 5의 배수라면
                    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < N and 0 <= nj < N:
                            v[ni][nj].append(1)
    # 겨울 : 양분추가
    for i in range(N):
        for j in range(N):
            arr[i][j] += add_arr[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(v[i][j])

print(ans)