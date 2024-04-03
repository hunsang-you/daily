'''
100

2

'''
# 수학, 정수론

import sys
input = sys.stdin.readline

N = int(input())


temp = 0
for i in range(2, N//2 + 1):
    temp += i * (N // i - 1) % 1000000

print(temp % 1000000)