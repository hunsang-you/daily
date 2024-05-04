'''
8
20
42
0

'''
# 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

prime = [1] * 1000001

for i in range(2, int(len(prime) ** 0.5) +1):
    if prime[i]:
        for j in range(2 * i, 1000001, i):
            prime[j] = 0

while True:
    N = int(input())
    if N == 0:
        break

    for i in range(N-3, 2, -2):
        if prime[i] == 1 and prime[N-i] == 1:
            print(f'{N} = {N-i} + {i}')
            break

    else:
        print('"Goldbach\'s conjecture is wrong."')