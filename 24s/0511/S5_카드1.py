'''
7

'''
# 구현, 자료구조, 큐

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

cards = deque(i for i in range(1, N+1))

ans = []

if N == 1:
    print(N)

else:

    while len(cards) > 1:
        now = cards.popleft()
        ans.append(now)

        next = cards.popleft()
        cards.append(next)
        if len(cards) == 1:
            last = cards.popleft()
            ans.append(last)
    print(*ans)