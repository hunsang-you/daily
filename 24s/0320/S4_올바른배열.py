'''
3
5
6
7

6
5
7
9
8492
8493
192398

4
1000
2000
3000
4000

7
6
1
9
5
7
15
8
'''
# 투 포인터

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
lst = []

for i in range(N):
    cnt = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            cnt += 1
    lst.append(cnt)

print(min(lst))
