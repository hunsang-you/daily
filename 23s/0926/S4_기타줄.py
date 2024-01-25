'''
4 2
12 3
15 4

10 3
20 8
40 7
60 4

15 1
100 40

17 1
12 3

7 2
10 3
12 2

9 16
21 25
77 23
23 88
95 43
96 19
59 36
80 13
51 24
15 8
25 61
21 22
3 9
68 68
67 100
83 98
96 57
'''

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
price = []
ans = 0
for _ in range(M):
    price.append(list(map(int, input().split())))

six_list = sorted(price, key=lambda x: x[0])
one_list = sorted(price, key=lambda x: x[1])


if six_list[0][0] <= one_list[0][1] * 6 :
    ans = six_list[0][0] * (N // 6) + one_list[0][1] * (N % 6)
    if six_list[0][0] < one_list[0][1] * (N % 6):
        ans = six_list[0][0] * (N//6 + 1)

else:
    ans = one_list[0][1] * N

print(ans)