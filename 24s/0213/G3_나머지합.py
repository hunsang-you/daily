'''
5 3
1 2 3 1 2

'''
# 누적합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

sumarr = []
divarr = []
temp = 0

for i in range(N):
    temp += arr[i]
    sumarr.append(temp)
    divarr.append(temp % M)

    if temp % M == 0:
        answer += 1

modcnt = [0] * M

for i in divarr:
    modcnt[i] += 1

for i in modcnt:
    answer += i * (i - 1) // 2

print(answer)