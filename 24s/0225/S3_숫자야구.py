'''
4
123 1 1
356 1 0
327 2 0
489 0 1

'''
# 브루트포스

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for _ in range(N):
    question, strike, ball = map(int, input().split())
    question = list(str(question))
    delete = 0

    for i in range(len(numbers)):
        strike_cnt, ball_cnt = 0, 0
        i -= delete
        for j in range(3):
            if question[j] == numbers[i][j]:
                strike_cnt += 1

            elif question[j] in numbers[i]:
                ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            numbers.remove(numbers[i])
            delete += 1

print(len(numbers))

