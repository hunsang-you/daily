'''
60
100

64
65
'''
# 소수 판정
# 자연수 M,N이 주어질 때 M 이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾아라
# EX) M=60 N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

result = []

for i in range(M, N+1):
    for j in range(2, i+1):
        if i == j : # 소수일 경우 추가
            result.append(i)

        elif i % j == 0:     # 소수가 아닐경우
            break

if len(result) == 0:
    print(-1)

else:
    print(sum(result))
    print(min(result))