'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N+1)]
D = [[0] * (N+1) for _ in range(N+1)]

for i in range(N):
    arrrow = [0] + [int(x) for x in input().split()]
    arr.append(arrrow)

for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)