'''
0 0 0 1 1 0

0 0 4 0 0 3

0 0 1 0 47 0

1 2 3 4 8 7

2 -1 -7 2 -1 0

'''
# 수학, 기하학, 피타고라스 정리

import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())

ans = 0.0

if x1 == x2 == x3 or y1 == y2 == y3:
    ans = -1.0

elif y1 - y2 != 0 and y1 - y3 != 0 and y2 - y3 != 0 and (x1 - x2)/(y1 - y2) == (x2 - x3)/(y2 - y3) == (x1- x3)/(y1 - y3):
    ans = -1.0

else:
    d1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    d2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** (1/2)
    d3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** (1/2)

    ans = max(d1, d2, d3) * 2 - min(d1, d2, d3) * 2

print(ans)