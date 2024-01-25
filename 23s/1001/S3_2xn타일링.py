'''
2

9
'''
# dp
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수

import sys
input = sys.stdin.readline

# n = 1 > 1  n = 2 > 2  n = 3 > 3   n = 4 > 5
N = int(input())

A = [0] * 1001

A[1] = 1
A[2] = 2

for i in range(3, 1001):
    A[i] = (A[i-1] + A[i-2]) % 10007

print(A[N])