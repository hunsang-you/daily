'''
3 5
42101
22100
22101
2 2
12
34
2 4
1255
3455
'''
N, M = map(int, input().split())
board=[list(map(int, input())) for _ in range(N)]
answer = []

for i in range(N):
    for j in range(M):
        dot = board[i][j]
        for k in range(j, M):
            if board[i][k] == dot and i + k - j < N and k < M:
                if board[i + k - j][j] == dot and board[i + k - j][k] == dot:

                    answer.append((k - j + 1) ** 2)

print(max(answer))