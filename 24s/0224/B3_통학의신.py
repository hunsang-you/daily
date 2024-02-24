'''
2 3

1 -8

1 1
'''
# 브루트포스

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
answer = []

x1 = int((-(2 * A) + (((2 * A) ** 2) - (4 * B)) ** 0.5) // 2)
x2 = int((-(2 * A) - (((2 * A) ** 2) - (4 * B)) ** 0.5) // 2)

if x1 < x2 :
    print(x1, x2)

elif x1 > x2 :
    print(x2, x1)

elif x1 == x2:
    print(x1)