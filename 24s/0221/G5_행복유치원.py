'''
5 3
1 3 5 6 10
'''
# 그리디

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tall = list(map(int, input().split()))

union = []

for i in range(1, N):
    union.append(tall[i] - tall[i-1])

union.sort()

answer = 0
for i in range(N-K):
    answer += union[i]

print(answer)