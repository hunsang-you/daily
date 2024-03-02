'''
176 177

5 9

25 28
'''
# 수학

import sys
input = sys.stdin.readline


A, B = map(int, input().split())

def calc(n):
    # 숫자가 0이면 나눌수 없음
    if n == 0:
        return 0

    # 숫자가 1이면 2^0이므로 1
    elif n == 1:
        return 1

    # 숫자가 짝수인 경우 계속 반복
    elif n % 2 == 0:
        return n // 2 + 2 * calc(n // 2)

    # 1이 아닌 홀수인 경우 반복
    else:
        return (n // 2 + 1) + 2 * calc(n // 2)

print(calc(B) - calc(A-1))