'''
2 3
123
456

5 5
00000
00000
00200
00000
00000

6 7
3791178
1283252
4103617
8233494
8725572
2937261

5 9
135791357
357913579
579135791
791357913
913579135

9 9
553333733
775337775
777537775
777357333
755553557
355533335
373773573
337373777
775557777

9 9
257240281
197510846
014345401
035562575
974935632
865865933
684684987
768934659
287493867
'''
import sys
from math import sqrt
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]

result = -1

for i in range(N):
    for j in range(M):
        for a in range(-N, N):
            for b in range(-M, M):
                num = ""
                y, x = i, j
                while 0 <= x < M and 0 <= y < N:
                    num += str(board[y][x])
                    if a == 0 and b == 0:
                        break
                    if int(sqrt(int(num))) ** 2 == int(num):
                        result = max(int(num), result)
                    y += a
                    x += b
print(result)