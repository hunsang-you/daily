'''
13

14

'''
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘

import sys
input = sys.stdin.readline

N = int(input())

five = 0
two = 0
while True:
    if N % 5 == 0:
        five += N // 5
        break
    else:
        N -= 2
        two += 1

    if N < 0:
        break

if N < 0:
    print(-1)

else:
    print(five + two)

