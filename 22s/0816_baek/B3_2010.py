# 플러그
# python 으로 제출하면 시간초과가 뜨기때문에 pypy3로 제출했다.

N = int(input())
result = 0
for i in range(N):
    plug = int(input())
    result += plug
print(result-(N-1))
