'''
4
2
4
5
231


'''
# 수학, 정수론, 누적 합, 유클리드 호제법
import sys
input = sys.stdin.readline

C = int(input())

def GCD(i, j):
    if j == 0:
        return i
    return GCD(j, i % j)

DP = [0] * 1001
DP[1] = 3

for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i != j and GCD(i, j) == 1:
            cnt += 2

    DP[i] = DP[i-1] + cnt

for _ in range(C):
    N = int(input())
    print(DP[N])
