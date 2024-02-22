'''
5
1 2 2 1 2
1 5
'''
# 그래프이론, 탐색, BFS

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
a, b = map(int, input().split())

answer = 0
def BFS(a, b):
    queue = deque([a-1])
    visited = [-1] * (N+1)
    visited[a-1] = 0

    while queue:
        now = queue.popleft()

        # 우측방향
        for i in range(now, N, arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1

                if i == b-1:
                    return visited[i]
        # 좌측방향
        for i in range(now, -1, -arr[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
                if i == b-1:
                    return visited[i]


    return -1

print(BFS(a, b))
