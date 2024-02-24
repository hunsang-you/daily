'''
4 7
20 15 10 17

5 20
4 42 40 26 46
'''
# 이분탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 1, max(trees)

while left <= right:
    mid = (left + right) // 2
    temp = 0
    # 나무의 길이가 mid 보다 길면 잘라서 temp에 더하기
    for tree in trees:
        if tree >= mid:
            temp += tree - mid

    # temp의 길이가 M보다 크면 최대한 작게 temp를 만들어야 하므로 left를 mid+1로 조정
    # temp의 길이가 M보다 작으면 높이를 늘리기 위해 right = mid + 1
    if temp >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)