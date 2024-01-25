# 각 자리수를 내림차순으로 정렬한다.
'''
2143 -> 4321
999998999 -> 999999998
61423 -> 64321
'''

N = list(map(int, input()))

for i in range(len(N)):
    for j in range(1, len(N)):
        if N[j-1] < N[j]:
            N[j-1], N[j] = N[j], N[j-1]

for i in N:
    print(i, end='')