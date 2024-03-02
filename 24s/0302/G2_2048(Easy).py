'''
3
2 2 2
4 4 4
8 8 8
'''
# 구현, 브루트포스, 시뮬레이션, 백트래킹

import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def move(board):        # 행단위로 이동(같은값 합치기)
    for i in range(len(board)): # 행 개수만큼 처리
        num = 0                 # append해야할 기준숫자(같으면 두배로)
        temp_lst = []
        for n in board[i]:      # 행에서 숫자 하나씩 처리
            # 빈칸은 당연히 처리안함
            if n == 0:
                continue
            if n == num:        # 기준 숫자와 같은 경우 합침(이후 기준이 0)
                temp_lst.append(num*2)
                num = 0
            else:               # 기준숫자와 다른경우
                if num == 0:    # 처음 숫자를 만난경우
                    num = n

                else:
                    temp_lst.append(num)
                    num = n
        # 종료 후 기준숫자 있으면 temp_lst추가 그리고 남은자리 0
        if num > 0:     # 마지막에 숫자추가
            temp_lst.append(num)
        board[i] = temp_lst + [0] * (N-len(temp_lst))     # temp_lst 남은 길이를 0으로 채움



def DFS(n, arr):
    global ans
    # 종료조건: 5번 처리 완료
    if n == 5:
        ans = max(ans, max(map(max, arr)))      # board 중 가장 큰값으로 갱신
        return

    # 좌측이동(좌측으로 기울이기)
    Narr = [lst[:] for lst in arr]      # 딥카피해서 전달
    move(Narr)
    DFS(n+1, Narr)

    Narr = [lst[::-1] for lst in arr]   # 우측
    move(Narr)
    DFS(n+1, Narr)

    arr_t = list(map(list, zip(*arr)))  # 열 => 행으로 처리
    Narr = [lst[::] for lst in arr_t]    # 상방향 딥카피
    move(Narr)
    DFS(n+1, Narr)

    Narr = [lst[::-1] for lst in arr]    # 상방향 딥카피
    move(Narr)
    DFS(n+1, Narr)

    # 상하좌우 네방향(가능한 모든경우 처리)

DFS(0, board)
print(ans)