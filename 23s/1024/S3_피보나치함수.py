'''
3
0
1
3

2
6
22
'''
# DP
import sys
input = sys.stdin.readline

def fibonacci(N):
    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero + one
    print(zero, one)
T = int(input())
dp = [0 for _ in range(T+1)]

for _ in range(T):
    N = int(input())
    fibonacci(N)