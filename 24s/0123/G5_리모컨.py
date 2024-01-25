'''
5457
3
6 7 8

100
5
0 1 2 3 4

500000
8
0 2 3 4 6 7 8 9

100
3
1 0 5

14124
0

1
9
1 2 3 4 5 6 7 8 9

80000
2
8 9
'''
# 브루트포스

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

broken = list(map(int, input().split()))


min_cnt = abs(100 - N)

for i in range(1000001):
    num = str(i)

    for j in range(len(num)):
        if int(num[j]) in broken:
            break

        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(int(num) - N) + len(num))

print(min_cnt)