'''
5 2
1 4 2 5 1

7 5
1 1 1 1 1 5 1

5 3
0 0 0 0 0

'''
# 누적 합, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

sum_ = sum(arr[:X])
temp = sum_

day = 1
for i in range(X, N):
    temp -= arr[i - X]
    temp += arr[i]

    if sum_ < temp:
        sum_ = temp
        day = 1

    elif sum_ == temp:
        day += 1


if sum_ > 0:
    print(sum_)
    print(day)

else:
    print("SAD")
