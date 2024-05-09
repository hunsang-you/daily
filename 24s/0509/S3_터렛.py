'''
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5

'''
# 수학, 기하학, 많은 조건분기

import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 원의 중심 사이의 거리
    distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)

    if distance == 0:   # 두 원의 중심이 겹치면
        if r1 == r2:        # 두 원의 크기까지 겹치는 경우
            print(-1)

        else:               # 두 원의 크기는 다른 경우 = 겹치는 부분이 x
            print(0)


    else:               # 두 원의 중심이 다른경우
        if r1 + r2 == distance or abs(r1 - r2) == distance:
            print(1)

        elif abs(r1 - r2) < distance and distance < r1 + r2:
            print(2)

        else:
            print(0)