'''
3 1
4 4 2

4 2
9 7 9 1

4 4
1 1 1 1
'''
# 백트래킹
# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# N개의 자연수 중에서 M개를 고른 수열

N, M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))
visited = [0] * N
temp = []


def backtracking():
    if len(temp) == M :
        print(*temp)
        return
    num = 0
    for i in range(N):
        if visited[i] == 0 and num != numbers[i] :
            visited[i] = 1
            temp.append(numbers[i])
            num = numbers[i]
            backtracking()
            visited[i] = 0
            temp.pop()

backtracking()