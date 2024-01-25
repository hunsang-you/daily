'''
4
0 0
0 10
10 10
10 0

'''
import sys
input = sys.stdin.readline

x, y = [], []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

nx, ny = 0, 0
for i in range(N):
    nx += x[i] * y[i+1]
    ny += y[i] * x[i+1]

print(round(abs((nx-ny)/2),1))