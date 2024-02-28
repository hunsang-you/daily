'''
10 1 10 2 1

100 2 1 1 0


'''
# 그래프이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
cnt = [0 for _ in range(F+1)]
def BFS(v):
    global cnt
    queue = deque([v])
    visited[v] = 1
    while queue:
        now = queue.popleft()

        if now == G:
            return cnt[G]

        else:
            for i in (now+U, now-D):
                if 1 <= i <= F and visited[i] == 0:
                    visited[i] = 1
                    cnt[i] = cnt[now] + 1
                    queue.append(i)
    if cnt[G] == 0:
        return "use the stairs"

print(BFS(S))

