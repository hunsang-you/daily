'''
3 1
4 2
4 4
'''
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

N, M = map(int, input().split())

pair = []

def func(s):
    if len(pair) == M :         # pair의 길이가 M이라면 출력
        return print(*pair)

    for i in range(1, N+1):     # 만약 N까지의 숫자중 새 리스트에 없다면 i 추가한다.
        if i not in pair :      # i가 리스트에 없다면 추가하고 함수를 다시 실행한다.
            pair.append(i)
            func(i)
            pair.pop()

func(1)
