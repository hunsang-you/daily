'''
100

189

'''
# 수학 구현 그리디
A, B, C = 300, 60, 10

T = int(input())
a, b, c = 0, 0, 0
while T > 0:
    if T % 10 != 0:
        print(-1)
        exit()

    if T >= 300 :
        a += 1
        T -= 300

    elif T >= 60 :
        b += 1
        T -= 60

    else:
        c += 1
        T -= 10

print(a, b, c)