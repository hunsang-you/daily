'''
20

3

41

53

'''
# 수학, 정수론, 투 포인터, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

N = int(input())
prime = [0, 0] + [1] * (N-1)
prime_num = []

for i in range(2, N+1):
    if prime[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            prime[j] = 0


answer = 0
l, r = 0, 0

while r <= len(prime_num):
    temp = sum(prime_num[l:r])

    if temp == N:
        answer += 1
        r += 1

    elif temp < N:
        r += 1

    else:
        l += 1

print(answer)