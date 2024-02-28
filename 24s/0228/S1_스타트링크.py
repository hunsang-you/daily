'''
10 1 10 2 1

100 2 1 1 0


'''
# 그래프이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque


F, S, G, U, D = map(int, input().split())
cnt = 0
def BFS():
    global cnt
    queue = deque()
    queue.append(S)
    while queue:
        now = queue.popleft()

        if 1 <= now <= G:
            if now < G and now + U < G:
                now += U
                cnt += 1
                queue.append(now)
            elif now > G and now - D > 1 :
                now -= D
                cnt += 1
                queue.append(now)
            elif now == G:
                return cnt

            print(now, cnt)
BFS()
print(cnt)