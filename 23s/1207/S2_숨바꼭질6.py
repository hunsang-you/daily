'''
3 3
1 7 11

3 81
33 105 57

1 1
1000000000
'''
# 유클리드 호제법
import sys
input = sys.stdin.readline

from math import gcd
N,S = map(int,input().split())
lst = list(map(int,input().split()))
g = abs(lst[0]-S)

for i in lst[1:]:
    g = gcd(abs(i-S),g)
print(g)