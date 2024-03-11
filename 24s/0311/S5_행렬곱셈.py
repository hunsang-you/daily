'''
3 2
1 2
3 4
5 6
2 3
-1 -2 0
0 0 3

'''
# 수학, 구현, 선형대수학

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for i in range(M):
    B.append(list(map(int, input().split())))

# 행렬 곱셈
C = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for i in range(N):
    for j in C[i]:
        print(j, end=" ")
    print()