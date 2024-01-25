'''
4
3 1 4 2
2 2 3 3

3
1 1 5
4 2 1

2
2 1
2 1
'''
import sys
input = sys.stdin.readline


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []

for i in range(N):
    arr.append(abs(A[i]-B[i]))

print(sum(arr)//2)