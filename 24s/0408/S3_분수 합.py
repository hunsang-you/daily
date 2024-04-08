'''
2 7
3 5

'''
# 수학, 정수론, 유클리드 호제법

import sys
input = sys.stdin.readline

# A/B C/D
A, B = map(int, input().split())
C, D = map(int, input().split())

def GCD(a, b):
    tmp = a % b
    while tmp > 0:
        a = b
        b = tmp
        tmp = a % b
    return b


numer = (B * C + A * D)
denom = B * D


# 분자 분모의 최대공약수 구하기
gcd = GCD(numer, denom)

print(numer//gcd, denom//gcd)