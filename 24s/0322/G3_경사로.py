'''
6 2
3 3 3 3 3 3
2 3 3 3 3 3
2 2 2 3 2 3
1 1 1 2 2 2
1 1 1 3 3 1
1 1 2 3 3 2

6 2
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

6 3
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

6 1
3 2 1 1 2 3
3 2 2 1 2 3
3 2 2 2 3 3
3 3 3 3 3 3
3 3 3 3 2 2
3 3 3 3 2 2

'''
# 구현

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 전치행렬로 열 => 행처리, 양바향 처리로 (역방향도 처리)
ans = 0

def check(lst, visited):
    cnt = 1     # 연속된 동일 숫자의 개수
    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:      # 높이가 같은경우
            cnt += 1
        # 높이가 1차이 인 경우 -> 경사로를 놓을수 있는지 확인
        # 1 증가하고, 연속된 길이가 경사로의 길이보다 같거나 길며, 겹쳐서 놓지 않을 수 있다면
        elif lst[i-1] + 1 == lst[i] and cnt >= L and visited[i-L:i] == [0] * L:
            cnt = 1             # 바뀐높이 카운트 다시시작
            visited[i-L:i] = [1] * L

        elif lst[i-1] > lst[i]:         # 내려가는 경우 => 반대방향에서 고민
            cnt = 1

        else:               # 높이가 2 이상 차이인 경우 => 불가능
            return False

    return True


# 가로방향
for _ in range(2):
    for lst in board:
        visited = [0] * len(lst)      # 미방문리스트(겹쳐서 놓기 방지용)
        # 증가방향도 성공 and 감소방향(반대방향)도 성공이면 가능한 길
        if check(lst, visited) and check(lst[::-1], visited[::-1]):
            ans += 1

        # 열의 행처리를 위해 전치행렬 변환
    board = list(map(list, zip(*board)))


print(ans)
