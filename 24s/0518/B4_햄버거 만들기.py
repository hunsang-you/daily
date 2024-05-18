'''
6 3

5 4

1 7

'''
# 수학, 사칙연산

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

ans = 0

while A >= 2 and B >= 1:
    A -= 2
    B -= 1
    ans += 1

print(ans)