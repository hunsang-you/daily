'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
# visited = [0] * N

num = []



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0

    if board[x][y] == 1 :
        global cnt
        cnt += 1
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return 1
    return 0

result = 0      # 총 단지 수
cnt = 0         # 단지에 속한 집의 수
for i in range(N):
    for j in range(N):
        if DFS(i, j) == 1:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)

for i in range(len(num)):
    print(num[i])
