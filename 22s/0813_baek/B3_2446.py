# 별찍기 - 6

N = int(input())

for i in range(N) :
    print(" " * i + "*" * ((N - i) * 2 -1))

for i in range(N-2, -1, -1) :
    print(" " * i + "*" * ((N - i) * 2 -1))


