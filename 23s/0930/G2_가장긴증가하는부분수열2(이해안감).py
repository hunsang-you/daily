'''
6
10 20 10 30 20 50
'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
dp[0] = A[0]