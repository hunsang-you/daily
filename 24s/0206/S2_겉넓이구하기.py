'''
1 1
1

3 3
1 3 4
2 2 3
1 2 4
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

square = [list(map(int, input().split())) for _ in range(N)]

left = 0
right = 0
updown = N * M

for i in range(N):
    for j in range(M):
        if j == 0:
            left += square[i][j]

        else :
            if square[i][j] > square[i][j-1]:
                left += square[i][j] - square[i][j-1]


for i in range(M):
    for j in range(N):
        if j == 0:
            right += square[j][i]
        else:
            if square[j][i] > square[j-1][i] :
                right += square[j][i] - square[j-1][i]

print((left+right+updown) * 2)