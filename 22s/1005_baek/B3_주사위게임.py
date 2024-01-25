'''
4
5 6
6 6
4 3
5 2
'''
N = int(input())
A_score = 100
B_score = 100
for _ in range(N):
    A, B = map(int, input().split())

    if A > B :
        B_score -= A

    elif A < B :
        A_score -= B



print(A_score)
print(B_score)