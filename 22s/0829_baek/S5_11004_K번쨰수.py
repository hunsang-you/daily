'''
5 2
4 1 2 3 5
'''

N, K = map(int, input().split())

A = list(map(int, input().split()))

A = sorted(A)

for i in range(len(A)):
    if i+1 == K :
        print(A[i])

# print(A)