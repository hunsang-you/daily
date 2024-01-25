# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다
N, M = map(int, input().split())

pair = []

def func(s):
    if len(pair) == M:          # pair의 길이가 M이라면 출력
        return print(*pair)

    for i in range(s, N+1):         # i를 s부터 시작하여 첫 pair[0]보다 작은 숫자가 추가되지 않게한다.
        if i not in pair:           # 만약 N까지의 숫자중 새 리스트에 없다면 i 추가한다.
            pair.append(i)
            func(i)
            pair.pop()

func(1)
