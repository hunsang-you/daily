'''
1
10
13
100
1000
10000
100000
0
'''
# 에라토스테네스의 체
# 베르트랑 공준은 임의의 자연수 N에 대하여, N보다 크고, 2N보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고있다.
# EX) 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19)
# EX) 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17, 19, 23)
# 자연수 N이 주어졌을 때의 베르트랑 공준을 구하라

import sys
input = sys.stdin.readline


num = 123456 * 2 + 1
arr = [1]*num

for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            arr[i] = 0
            break

while True:
    N = int(input())

    if N == 0:
        break

    cnt = 0

    for i in range(N+1, 2*N+1):
        cnt += arr[i]
    print(cnt)