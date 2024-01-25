'''
100 50

1 1

17 5

2 4

20 4
'''

N, M = map(int, input().split())

answer = 0
if N == 1:
    answer = 1

elif N == 2:
    if M >= 1 and M <= 6:
        answer = (M + 1) // 2
    elif M >= 7:
        answer = 4

elif N >= 3:
    if M <= 6 :
        answer = min(M, 4)

    elif M >= 7:
        answer = M - 2

print(answer)