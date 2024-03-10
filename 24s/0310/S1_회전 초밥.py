'''
8 30 4 30
7
9
7
30
2
7
9
25

8 50 4 7
2
7
9
25
7
9
7
30
'''
# 브루트포스, 투 포인터, 슬라이딩 윈도우
# pypy
import sys
input = sys.stdin.readline

# 초밥의수, 초밥의 종류, 연속해서 먹는 접시수, 쿠폰번호
N, D, K, C = map(int, input().split())

belt = [int(input()) for _ in range(N)]

left, right = 0, 0
ans = 0

while left != N:
    right = left + K
    select = set()
    coupon = True
    for i in range(left, right):
        i %= N
        select.add(belt[i])
        if belt[i] == C:
            coupon = False

    cnt = len(select)
    if coupon == True:
        cnt += 1

    ans = max(ans,cnt)
    left += 1

print(ans)