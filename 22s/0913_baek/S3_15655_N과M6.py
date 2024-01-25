# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
'''
3 1
4 5 2

4 2
9 8 7 1

4 4
1231 1232 1233 1234
'''
def func(s):
    if len(pair) == M :
        return print(*pair)

    for i in range(s, N) :
        if nums[i] not in pair :
            pair.append(nums[i])
            func(i+1)
            pair.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
pair = []

func(0)