'''
122333444455555


'''
# 수학, 이분탐색
N = int(input())

ans = 0
left, right = 0, N
while left <= right:
    mid = (left + right) // 2

    if mid ** 2 < N:
        left = mid + 1

    else:
        right = mid - 1


print(left)