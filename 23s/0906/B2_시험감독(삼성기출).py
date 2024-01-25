'''
1
1
1 1

3
3 4 5
2 2

5
1000000 1000000 1000000 1000000 1000000
5 7

5
10 9 10 9 10
7 20

5
10 9 10 9 10
7 2
'''

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = N

for i in range(N):
    A[i] = A[i] - B
    if A[i] > 0 :
        if A[i] % C == 0 :
            cnt += A[i] // C
        elif A[i] % C != 0:
            cnt += A[i] // C + 1


print(cnt)