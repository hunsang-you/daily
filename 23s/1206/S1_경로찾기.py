'''
3
0 1 0
0 0 1
1 0 0

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
'''
# 그래프이론 최단경로 플로이드–워셜
# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if board[j][i] and board[i][k]:
                board[j][k] = 1

for i in board:
    print(*i)