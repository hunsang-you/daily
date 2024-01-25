'''
3 8
WEAK 10000
NORMAL 100000
STRONG 1000000
0
9999
10000
10001
50000
100000
500000
1000000

3 5
B 100
A 100
C 1000
99
100
101
500
1000
'''
# 이분탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = [input().split() for _ in range(N)]
name.sort(key=lambda x:int(x[1]))

powers = [int(input()) for _ in range(M)]

for power in powers:
    left, right = 0, len(name)
    result = 0

    while left <= right:
        center = (left + right) // 2
        if int(name[center][1]) >= power:
            result = center
            right = center - 1

        else:
            left = center + 1

    print(name[result][0])
