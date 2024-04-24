'''
3
124
25
194

'''
# 수학, 그리디 알고리즘, 사칙연산

import sys
input = sys.stdin.readline

N = int(input())
coin = [25, 10, 5, 1]
for _ in range(N):
    money = int(input())
    ans = []
    for i in coin:
        ans.append(money // i)
        money = money % i

    print(*ans)