'''
5
6
8
10
12
100

'''
# 수학, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

prime = [0] + [0] + [1] * 1000000

for i in range(1, 1000001):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            prime[j] = 0


T = int(input())
for i in range(T):
    N = int(input())
    cnt = 0
    for j in range(2, N//2 + 1):
        if prime[j] == 1 and prime[N-j] == 1:
            cnt += 1

    print(cnt)

