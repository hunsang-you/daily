'''
10 11 12
'''
def func(a, b, c):
    if b == 1:
        return a % c

    elif b % 2 == 0:
        return (func(a, b//2, c) ** 2) % c

    else :
        return ((func(a, b//2, c) ** 2) * a) % c

A, B, C = map(int, input().split())

print(func(A,B,C))
