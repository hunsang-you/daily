'''
18

0

500000
'''
# 브루트포스, 백트래킹
import sys
input = sys.stdin.readline
from itertools import combinations
N = int(input())
result = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        num = sorted(list(j), reverse=True)
        result.append(int("".join(map(str, num))))

result.sort()
if len(result) > N:
    print(result[N])

else:
    print(-1)
