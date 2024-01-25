'''
10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5
'''
# DP
# N개의 정수로 이루어진 임의의 수열
# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰합(단 수는 한개 이상 선택)
# EX) 10, -4, 3, 1, 5, -35, 12, 21, -1 이라는 수열일 경우 12+21=33이 정답

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
dp = []
# arr[i] + arr[i+1] + arr[i+2] ....
# i번째 데이터 이전까지의 합을 계산, 최대값을 지속적으로 기록
# 이전까지의 합이, 그냥 i번째보다 작은 경우 이전의 기록은 무의미

for i in range(1, N):
    arr[i] = max(arr[i], arr[i] + arr[i-1])
print(max(arr))