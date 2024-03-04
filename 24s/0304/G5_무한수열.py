'''
7 2 3

0 2 3

10000000 3 3

256 2 4

1 1000000 1000000
'''
# DP, 자료구조, 해시를 이용한 집합과 앱

import sys
input = sys.stdin.readline

N, P, Q = map(int, input().split())

dict = {}

dict[0] = 1

def func(num):
    # N값이 있다면 반환
    if num in dict:
        return dict[num]

    # 없다면 계산해서 넣어줌
    else:
        dict[num] = func(num//P) + func(num//Q)

        return dict[num]

print(func(N))

