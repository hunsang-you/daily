'''
3
3
2
1

4
1
3
4
2

'''
# 구현, 브루트포스

import sys
input = sys.stdin.readline

N = int(input())

books = [int(input()) for _ in range(N)]

now = N
ans = 0
for i in range(N-1, -1, -1):
    if books[i] != now:
        ans += 1

    else:
        now -= 1

print(ans)