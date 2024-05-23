'''
3
1033 8179
1373 8017
1033 1033

'''
# 수학, 그래프 이론, 탐색, 정수론, BFS, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline
from collections import deque


def prime(x):
    if x == 1:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def BFS(A, B):
    queue = deque()
    queue.append((A, 0))
    while queue:
        password, cnt = queue.popleft()

        if password == B:
            return cnt

        for i in range(4):
            for j in range(10):
                new = list(str(password))
                new[i] = str(j)
                new = int(''.join(new))

                if 1000 <= new and visited[new] == 0 and prime(new):
                    visited[new] = 1
                    queue.append((new, cnt+1))

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    ans = BFS(A, B)

    print(ans)