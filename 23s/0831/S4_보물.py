'''
5
1 1 1 6 0
2 7 8 3 1
3
1 1 3
10 30 20
9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
'''

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    result += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(result)