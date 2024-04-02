'''
1 3 -1 4 1 7

2 5 8 3 -4 -11

'''
# 수학, 브루트포스

import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1001):
    for y in range(-999, 1001):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            break

