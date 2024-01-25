'''
2
2
0 0
1000 0
1000 1000
2000 1000
2
0 0
1000 0
2000 1000
2000 2000
'''
# 그래프이론, 그래프탐색, 너비 우선탑색(BFS)
# 출발은 상근이네 집에서 하고, 맥주 한 박스를 들고 출발한다.
# 맥주 한 박스에는 맥주가 20개 들어있다. 목이 마르면 안되기 때문에 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한 병을 마셔야 한다.

import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    queue = deque()
    queue.append([home[0], home[1]])
    while queue:
        x, y = queue.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(N):
            if visited[i] == 0:
                nx, ny = con[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append([nx, ny])
                    visited[i] = 1
    print("sad")
    return


t = int(input())
for i in range(t):
    N = int(input())
    home = [int(x) for x in input().split()]
    con = []
    for j in range(N):
        x, y = map(int, input().split())
        con.append([x, y])

    fest = [int(x) for x in input().split()]
    visited = [0 for i in range(N+1)]
    BFS()
