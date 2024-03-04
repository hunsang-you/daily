'''
2 4
CAAB
ADCB

3 6
HFDFFB
AJHGDH
DGAGEH

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
'''
# 그래프이론, 탐색, DFS, 백트래킹

import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]

answer = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
past = set(board[0][0])      # 알파벳 리스트
def DFS(x, y, cnt):
    global answer

    answer = max(answer, cnt)     # 지나온 알파벳이 많다면 교체

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 경계조건에 해당하는 것들중 지나가지 않은 칸만 반복
        if 0 <= nx < R and 0 <= ny < C :
            if board[nx][ny] not in past:
                past.add(board[nx][ny])      # 리스트에 없으므로 지나온 알파벳 추가
                DFS(nx, ny, cnt+1)
                past.remove(board[nx][ny])

    return answer

DFS(0, 0, 1)
print(answer)