'''
5
2
2 4

3
1
0

'''
# 구현, 이분탐색


import sys
input = sys.stdin.readline

N = int(input())        # 굴다리의 길이
M = int(input())        # 가로등의 개수
X = list(map(int, input().split()))         # 가로등의 위치

height = 0
# 가로등이 한개인 경우 모든곳을 다 비춰야함
if len(X) == 1:
    height = max(N-X[0], X[0])

else:
    height = X[0]
    for i in range(M):
        if i == M-1:
            temp = N - X[-1]            # 마지막 가로등의 위치에 따라 달라지는 거리 고려
        else:
            dist = X[i+1] - X[i]        # 가로등과 가로등 사이의 거리

            # dist가 홀수인 경우, 높이가 1 높아야 모든 거리를 비춤
            if dist % 2 == 1:
                temp = (dist // 2) + 1

            else:
                temp = dist // 2
        height = max(height, temp)

print(height)