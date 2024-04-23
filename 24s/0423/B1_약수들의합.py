'''
6
12
28
-1

'''
# 수학, 정수론, 구현

import sys
input = sys.stdin.readline


while True:
    N = int(input())

    if N == -1:
        break
    temp = []
    for i in range(1, N):
        if N % i == 0:
            temp.append(i)

    if sum(temp) == N:
        print(N,"=",end=" ")
        print(*temp,sep=" + ")

    else:
        print(N, "is NOT perfect.")
