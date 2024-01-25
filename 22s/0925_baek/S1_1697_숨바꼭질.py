'''
5 17
'''
from collections import deque
def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        X = queue.popleft()
        if X == K:
            print(road[X])
            break
        for nx in (X-1, X+1, X * 2):
            if 0 <= nx <= limit and not road[nx]:
                road[nx] = road[X] + 1
                queue.append(nx)

N, K = map(int, input().split())
limit = 100000
road = [0] * (limit + 1)

BFS()

