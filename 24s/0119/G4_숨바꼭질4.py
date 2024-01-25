'''
5 17

5 17
'''
# 그래프 이론, BFS

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
distance = [0] * 100001
move = [0] * 100001

def path(x):
    arr = []
    temp = x
    for i in range(distance[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def BFS():
    queue = deque()
    queue.append(N)

    while queue:
        x = queue.popleft()
        if x == K:
            print(distance[x])
            path(x)
            return
        for i in (x+1, x-1, 2*x):
            if 0 <= i <= 100000 and distance[i] == 0:
                queue.append(i)
                distance[i] = distance[x] + 1
                move[i] = x

BFS()
