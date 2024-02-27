'''
7 1
4 6
4 3

7 3
4 6
3 3
4 3
5 3

7 2
4 4
5 2
3 6

7 1
5 5
4 3

5 1
5 5
3 4
'''
# 구현

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
R, C = map(int, input().split())

# 상하좌우 및 대각선 방향
dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

move = [(R, C)]
for k in range(8):
    if 1 <= R + dx[k] <= N and 1 <= C + dy[k] <= N:
        move.append((R + dx[k], C + dy[k]))

immove = set()

for i in range(K):
    R_i, C_i = map(int, input().split())

    for nR, nC in move:
        if abs(nR-R_i) == abs(nC-C_i) or nR == R_i or nC == C_i:
            immove.add((nR, nC))


if (R, C) in immove:
    if len(move) == len(immove):
        print('CHECKMATE')

    else:
        print('CHECK')

else:
    if len(immove) == len(move)-1:
        print('STALEMATE')

    else:
        print('NONE')