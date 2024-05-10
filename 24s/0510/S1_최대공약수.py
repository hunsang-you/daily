'''
3 4

3 6

500000000000000000 500000000000000002

'''
# 수학, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(a, b):
    mod = a % b
    while mod != 0:
        a = b
        b = mod
        mod = a % b

    return b

print('1' * gcd(A, B))