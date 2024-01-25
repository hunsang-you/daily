'''
4 4
0100
0111
1110
0010
'''
# DP
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        if i == '0' or j == '0':
            dp[i][j] = int(board[i][j])

        elif board[i][j] == '0':
            dp[i][j] = 0

        else:
            dp[i][j] = min(int(dp[i - 1][j - 1]), int(dp[i - 1][j]), int(dp[i][j - 1])) + 1

        answer = max(dp[i][j], answer)

print(answer * answer)