'''
4
'''
# 백트래킹, 소수판정

import sys
input = sys.stdin.readline

N = int(input())

def func(num):
    if len(str(num)) == N:
        print(num)

    else:
        for i in range(10):
            temp = num * 10 + i

            if check(temp) == True:
                func(temp)

def check(num):
    for i in range(2, int(num ** 0.5) + 1):
        if int(num) % i == 0:
            return False
    return True


func(2)
func(3)
func(5)
func(7)