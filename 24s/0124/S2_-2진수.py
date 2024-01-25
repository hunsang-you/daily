'''
-13
'''

import sys
input = sys.stdin.readline

N = int(input())
answer = ''

if N == 0:
    print(0)

while N:
    if N % (-2) :
        N = (N // (-2)) + 1
        answer = '1' + answer

    else:
        N //= -2
        answer = '0' + answer

print(answer)