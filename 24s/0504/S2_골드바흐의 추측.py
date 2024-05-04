'''
3
8
10
16

'''
# 수학, 정수론, 소수 판정, 에라토스 테네스의 체

import sys
input = sys.stdin.readline


def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())

    l = N//2
    r = N - l

    while l > 0:
        if prime(l) and prime(r):
            print(l, r)
            break

        l -= 1
        r += 1
