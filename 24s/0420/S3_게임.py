'''
10 8

100 80

47 47

99000 0

1000000000 470000000

'''
# 수학, 이분탐색

import sys
input = sys.stdin.readline


# X - 게임횟수, Y - 이긴 게임(Z%)
X, Y = map(int, input().split())
Z = (Y * 100) // X
left, right = 0, X
ans = X
if Z >= 99:
    print(-1)

else:
    while left <= right:
        mid = (left + right) // 2
        if (100 * (Y+mid)) // (X + mid) > Z:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    print(ans)