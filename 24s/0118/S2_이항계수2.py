'''
5 2
'''
# DP

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 1
for i in range(K):
    answer *= N
    N -= 1

div = 1
for i in range(2, K+1):
    div *= i

print((answer // div) % 10007)