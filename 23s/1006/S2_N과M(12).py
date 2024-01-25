'''
3 1
4 4 2

4 2
9 7 9 1

4 4
1 1 2 2
'''
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
temp = []
visited = [0] * N
def backtracking(s):
    if len(temp) == M:
        print(*temp)
        return

    num = 0
    for i in range(s,N):
        if num != numbers[i]:
            temp.append(numbers[i])
            num = numbers[i]
            backtracking(i)
            temp.pop()
backtracking(0)