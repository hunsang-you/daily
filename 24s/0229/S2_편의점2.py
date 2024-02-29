'''
5
2 2
3 4
5 6
1 9
-2 -8

'''
# 정렬, 기하학

import sys
input = sys.stdin.readline

N = int(input())
customer = [list(map(int, input().split())) for _ in range(N)]

x_center = sorted(customer, key=lambda x:x[0])[N//2][0]
y_center = sorted(customer, key=lambda x:x[1])[N//2][1]

answer = 0

for i in customer:
    answer += (abs(x_center - i[0]) + abs(y_center - i[1]))

print(answer)
