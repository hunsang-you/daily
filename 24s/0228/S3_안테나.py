'''
4
5 1 7 9
'''
# 그리디, 정렬

import sys
input = sys.stdin.readline

N = int(input())

house = list(map(int, input().split()))
house.sort()

answer = house[(N-1) // 2]

print(answer)
