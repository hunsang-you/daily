'''
3
4
7
10
'''
def dp(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 4

    else :
        return dp(n-1) + dp(n-2) + dp(n-3)

T = int(input())
for test_case in range(T):
    N = int(input())

    print(dp(N))