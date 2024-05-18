'''
6 7
1
5
3
3
5
1

14 5
1
3
4
2
2
4
3
4
3
3
3
2
3
3

'''
# 투 포인터, 누적합

import sys
input = sys.stdin.readline

N, H = map(int, input().split())

# 구간별 충돌 수
lst = [0] * H

for i in range(N):
    h = int(input())
    # 종유석이라면
    if i % 2 == 0:
        lst[H-h] += 1
    # 석순이라면
    else :
        lst[0] += 1
        lst[h] -= 1

for i in range(1, H):
    lst[i] += lst[i-1]

ans = 0

min_pass = min(lst)

for i in lst:
    # 가장 적게 지나는 횟수와 같다면 증가
    if i == min_pass:
        ans += 1

print(min_pass, ans)