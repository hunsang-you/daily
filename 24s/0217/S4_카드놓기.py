'''
4
2
1
2
12
1

6
3
72
2
12
7
2
1
'''
# 백트래킹, 브루트포스

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
K = int(input())
cards = [input().rstrip() for _ in range(N)]
lst = set()

for i in permutations(cards, K):
    lst.add(''.join(i))
print(len(lst))