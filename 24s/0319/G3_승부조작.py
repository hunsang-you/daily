'''
5
1 1 0 1 0
1 1 0 0 0
1 0 2 1 0
1 0 2 1 0
0 1 0 0 1

4
0 1 1 1
1 0 1 0
0 2 0 1
1 0 0 0

'''
# 다이나믹 프로그래밍
# 0은 비어 있는 위치, 1은 흑돌, 2는 백돌.
import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
new_score = [[0] * N for _ in range(N)]

# def func():
#     global new_score
#     score = [[0] * N for _ in range(N)]
#     # 바꾸기전 가로 방향의 개수
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if board[i][j] == 1:
#                 cnt += 1
#                 score[i][j] = cnt
#             else:
#                 cnt = 0
#
#     # 세로방향
#     for i in range(N):
#         cnt = 0
#         for j in range(N):
#             if board[j][i] == 1:
#                 cnt += 1
#                 score[j][i] = max(score[j][i], cnt)
#             else:
#                 cnt = 0
#
#     # # 대각선(오른쪽 아래방향)
#     for k in range(N):
#         cnt = 0
#         for i in range(N-k):
#             j = i + k
#             if board[i][j] == 1:
#                 cnt += 1
#                 score[i][j] = max(score[i][j], cnt)
#             else:
#                 cnt = 0
#
#     # 대각선(오른쪽 위방향)
#     for k in range(N-1, -1, -1):
#         cnt = 0
#         for i in range(N):
#             j = N - 1 - i - k
#             if board[i][j] == 1:
#                 cnt += 1
#                 score[i][j] = max(score[i][j], cnt)
#             else:
#                 cnt = 0
#
#     for i in score:
#         new_score[max(i)] = max(i)
#
# for i in range(N):
#     for j in range(N):
#         if board[i][j] == 2:
#             board[i][j] = 1
#             func()
#             board[i][j] = 2
#
#
# print(max(new_score))
#
