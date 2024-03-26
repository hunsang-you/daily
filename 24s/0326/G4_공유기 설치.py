'''
5 3
1
2
8
4
9


'''
# 이분탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(1, N+1)]
house.sort()
left, right = 1, max(house) - min(house)
ans = 0
while left <= right:
    mid = (left + right) // 2
    now = house[0]
    cnt = 1

    # 공유기를 몇 대 설치할 수 있는지 체크
    for i in range(1, len(house)):
        if house[i] >= now + mid:
            cnt += 1
            now = house[i]

    if cnt >= C:
        left = mid + 1
        ans = mid

    else:
        right = mid - 1
print(ans)

