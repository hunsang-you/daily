'''
1

2

10

70

10000
'''

import sys
input=sys.stdin.readline

N = int(input())

sumNum = 0
for i in range(1, N+1):

    sumNum += (N//i)*i

print(sumNum)