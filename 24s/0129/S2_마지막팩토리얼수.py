'''
5
'''
# 수학
from math import factorial
import sys
input = sys.stdin.readline

N = (factorial(int(input())))
fac = list(str(N))

for i in fac[::-1]:
    if i != '0':
        print(i)
        break
