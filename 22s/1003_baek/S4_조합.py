'''
100 6
'''
def func(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

N, M = map(int, input().split())
print(func(N) // (func(M)*func(N-M)))


