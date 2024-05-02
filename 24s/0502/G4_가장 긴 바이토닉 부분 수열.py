'''
10
1 5 2 1 4 3 4 5 2 1

'''
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
reverse_arr = list(reversed(arr))

increase = [1 for i in range(N)]
decrease = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)

        if reverse_arr[i] > reverse_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(N)]

for i in range(N):
    result[i] = increase[i] + decrease[N-1-i] - 1

print(max(result))