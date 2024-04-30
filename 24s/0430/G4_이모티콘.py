'''
7 392

7 256

4 256

7 7

7 9

10 1

'''
# 그래프 이론, 탐색, BFS

import sys
input = sys.stdin.readline
from collections import deque

S, T = map(int, input().split())
visited = set()
visited.add(S)

def BFS(S):
    queue = deque()
    queue.append([S, ""])

    while queue:
        num, oper = queue.popleft()

        if num == T:
            return oper

        if num * num <= T and num * num not in visited:
            queue.append((num * num, oper+'*'))
            visited.add(num * num)

        if num * 2 <= T and num * 2 not in visited:
            queue.append((num * 2, oper+'+'))

        if num // num not in visited:
            queue.append((num//num, oper+'/'))

if S == T:
    print(0)
    exit()
ans = BFS(S)
if ans == None:
    print(-1)

else:
    print(ans)