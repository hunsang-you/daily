'''
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
'''
import math

T = int(input())
for _ in range(T):
    x1, y1, x2, y2, r1, r2 = map(int, input().split())

    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if d == 0 or r1 == r2 :
        print(-1)

    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    elif abs(r1-r2) < d < (r1+r2) :
        print(2)

    else:
        print(0)