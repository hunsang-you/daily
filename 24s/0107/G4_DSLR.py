'''
3
1234 3412
1000 1
1 16
'''
# 그래프이론
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b= map(int, input().split())

    visited = [0 for i in range(10001)]
    queue = deque()
    queue.append([a, ''])
    visited[a] = 1

    while queue:
        num, command = queue.popleft()

        if num == b:
            print(command)
            break
        d = num * 2 % 10000
        if visited[d] == 0:
            visited[d] = 1
            queue.append([d, command + 'D'])

        s = (num - 1) % 10000
        if visited[s] == 0:
            visited[s] = 1
            queue.append([s, command + 'S'])

        l = num // 1000 + (num % 1000) * 10
        if visited[l] == 0:
            visited[l] = 1
            queue.append([l, command + 'L'])

        r = num // 10 + (num % 10) * 1000
        if visited[r] == 0:
            visited[r] = 1
            queue.append([r, command + 'R'])
