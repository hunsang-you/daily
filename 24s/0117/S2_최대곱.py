'''
10 3

10 1

10 10

13 8

7 2
'''

import sys
input = sys.stdin.readline

S, K = map(int, input().split())

lst = [S // K for _ in range(K)]

for i in range(S % K):
    lst[i] += 1

answer = 1

for n in lst:
    answer *= n

print(answer)