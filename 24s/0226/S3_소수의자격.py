'''
10 15 3
'''
# 정수론, 에라토스테네스의 체, 소수판정

import sys
input = sys.stdin.readline

A, B, D = map(int, input().split())
lst = [True] * (B+1)
for i in range(2, int(B**0.5)+1):
    if lst[i]:
        for j in range(i+i, B+1, i):
            lst[j] = False

prime = []
for i in range(A, B+1):
    if lst[i]:
        prime.append(i)

ans = 0
for i in prime:
    if str(D) in list(str(i)):
       ans += 1

print(ans)