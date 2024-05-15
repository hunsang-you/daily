'''
31

'''
# 수학, 브루트포스 알고리즘, 정수론, 소수 판정, 에라토스테네스의 체

import sys
input = sys.stdin.readline

N = int(input())

def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

answer = 0
for i in range(N, 1000001):
    if i == 1:
        continue
    if prime(i) == True:
        if str(i) == str(i)[::-1]:
            answer = i
            break

if answer == 0:
    answer = 1003001
print(answer)

