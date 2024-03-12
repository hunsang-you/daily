'''
5 17
'''
# 그래프이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
line = [0] * (100001)
visited = [-1] * (100001)
visited[N] = 0
cnt = 0
def BFS(n, k):
    global cnt
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()

        if now == k:
            cnt += 1

        for next in [now-1, now+1, now*2]:
            if 0 <= next < 100001:
                if visited[next] == -1 or visited[next] >= visited[now] + 1:
                    visited[next] = visited[now] + 1
                    queue.append(next)

BFS(N, K)
print(visited[K])
print(cnt)