'''
6
10 20 10 30 20 50
'''
# DP 문제
# 수열A, 가장 긴 증가하는 부분수열을 구하는 프로그램
# EX) A {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, _10_, 30, _20_, 50} 이고 길이는 4이다.

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))