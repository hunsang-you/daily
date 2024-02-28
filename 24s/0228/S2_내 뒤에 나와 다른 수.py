'''
6
3 3 1 1 4 4
'''
# 자료구조

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
cnt = 1
num_id = []
for i in range(1, N):
    if arr[i-1] != arr[i] :
        num_id.append([i+1, cnt])
        cnt = 1

    else:
        cnt += 1

num_id.append([-1, cnt])


for id in num_id:
    print((str(id[0]) + ' ') * id[1], end='')