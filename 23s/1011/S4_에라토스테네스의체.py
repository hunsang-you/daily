'''
7 3

15 12

10 7
'''
# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numbers = [1] * (N+1)
# P = numbers[0]

tmp = 0
for i in range(2, N+1):
    for j in range(i, N+1, i):
        if numbers[j] != 0:
            numbers[j] = 0
            tmp += 1
            if tmp == K:
                print(j)