'''
6 180

2 86486400

'''
# 수학, 브루트포스, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline

# 최대 공약수 구하기
def GCD(a, b):
    while a % b != 0:       # 나머지가 0이 되는 순간 멈춘다.
        tmp = a % b
        a = b
        b = tmp

    return b

gcd, lcm = map(int, input().split())
div = lcm // gcd

a, b = 1, div

for i in range(1, div//2 + 1):
    if div % i == 0:
        A, B = i, div//i

        if GCD(A, B) != 1:
            continue
        if a + b > A + B:
            a = A
            b = B

print(a * gcd, b * gcd)
