'''
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4

3
1 0 -1
6
1 1
2 2
3 3
1 2
2 3
1 3


'''
# 누적 합

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lst = []
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    lst.append((i, j))

sum_ = [0] * (N+1)

for i in range(1, N+1):
    sum_[i] = sum_[i-1] + arr[i-1]


for i, j in lst:
    print(sum_[j] - sum_[i-1])