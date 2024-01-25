'''
8
'''
# 브루트포스, 백트래킹

N = int(input())
board = [0] * N
visited = [False] * N
result = 0
cnt = 0

def nqueen(depth):
    global result, cnt
    # depth == N 일때 N만큼의 퀸을 놓은것
    if depth == N:
        result += 1
        print(board, cnt)
        cnt += 1
        return

    # 해당 depth를 방문하지 않았을때
    for i in range(N):
        if visited[i] == False:
            board[depth] = i    # (depth, i)에 퀸 올리기 (depth = raw, i = column 해당)

            if check(depth) == True:
                visited[i] = True
                nqueen(depth+1)             # 다음열로 넘어가서 백트래킹
                visited[i] = False

# 모든 열과 대각선, 좌우에 위치해 있는지 확인
def check(N):
    global cnt
    for i in range(N):

        if board[N] == board[i] or N-i == abs(board[N]-board[i]):
            return False

    return True

nqueen(0)
print(result)