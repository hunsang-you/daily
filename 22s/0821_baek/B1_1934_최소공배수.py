T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    lst = []

    for i in range(1, min(A,B) + 1):
        if A % i == 0 and B % i == 0 :
            lst.append(i)

    LCM = A * B // max(lst)

    print(LCM)

