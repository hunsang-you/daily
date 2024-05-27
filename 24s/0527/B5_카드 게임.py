'''
1
2
3
4
5

0
100
0
10
100

'''
# 수칙, 사칙연산

import sys
input = sys.stdin.readline

ans = 0
for i in range(5):
    num = int(input())
    ans += num

print(ans)