'''
6
10 30 10 20 20 10
'''
# DP
# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하기
# EX) A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {30, 20, 10} 이고 길이는 3이다

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(dp)