# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 2번과는 다르게 (i, i)가 들어갈 수 있다.
def func(s):
    if len(pair) == M:
        return print(*pair)

    for i in range(s, N+1):     # i는 s부터 시작하여 s보다 작은 값은 추가하지 않는다.
        pair.append(i)
        func(i)
        pair.pop()


N, M = map(int, input().split())

pair = []


func(1)