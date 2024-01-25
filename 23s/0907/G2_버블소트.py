'''
5
10
1
5
2
3

5
1
3
5
7
9
'''

import sys

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append((int(input()), i))

Max = 0
Sarr = sorted(arr)

for i in range(N):
    if Max < Sarr[i][1] - i:
        Max = Sarr[i][1] - i

print(Max+1)