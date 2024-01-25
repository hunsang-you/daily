'''
10
1 100 2 50 60 3 5 6 7 8
'''
# DP
# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하시오ㅓ
# EX) A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
dp[0] = A[0]

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i] :
            dp[i] = max(dp[i], dp[j] + A[i])
        else:
            dp[i] = max(dp[i], A[i])

print(max(dp))