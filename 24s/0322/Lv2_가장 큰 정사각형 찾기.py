def solution(board):
    N = len(board)
    M = len(board[0])
    DP = [[0] * M for _ in range(N)]
    DP[0] = board[0]
    for i in range(1, N):
        DP[i][0] = board[i][0]
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 1:
                DP[i][j] = min(DP[i - 1][j - 1], DP[i - 1][j], DP[i][j - 1]) + 1

    temp = 0
    for i in DP:
        temp = max(max(i), temp)
    answer = temp ** 2

    return answer