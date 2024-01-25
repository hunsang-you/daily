# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다
# 중복 가능
# 1번에서 if조건만 제거하면 된다.

N, M = map(int, input().split())

pair = []

def func(s):
    if len(pair) == M:
        return print(*pair)


    for i in range(1, N+1):
        # 중복이 가능하므로 if i not in pair를 넣지않고 실행한다.
        pair.append(i)
        func(i)
        pair.pop()

func(1)