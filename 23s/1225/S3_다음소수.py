'''
3
6
20
100
'''
# 브루트포스, 소수판정

import math
import sys
input = sys.stdin.readline

def func(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


N = int(input())
for i in range(N):
    num = int(input())
    while True:
        if func(num):
            print(num)
            break
        else:
            num += 1