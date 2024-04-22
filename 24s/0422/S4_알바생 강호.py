'''
4
3
3
3
3

3
3
2
3

5
7
8
6
9
10

5
1
1
1
1
2

3
1
2
3

'''
# 그리디, 정렬

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
tip = 0

arr.sort(reverse=True)

for i in range(1, N+1):     # 입장순서
    if arr[0] - (i-1) > 0:      # 팁이 양수
        tip += arr[0] - (i-1)   # 팁 추가
        arr.pop(0)

    else:
        arr.pop(0)
print(tip)
