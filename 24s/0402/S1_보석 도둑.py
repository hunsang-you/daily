'''
15
'''
# 수학, 정수론, 소수 판정, 에라토스테네스의 체


import sys
from math import ceil, sqrt
input = sys.stdin.readline

K = int(input())
lst = []
for i in range(2, ceil(sqrt(K)) + 1):
    while K % i == 0 :
        lst.append(i)
        K //= i

if K != 1:
    lst.append(K)

print(len(lst))
print(*lst)