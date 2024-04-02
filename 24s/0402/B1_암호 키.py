'''
3
1000036000099
1500035500153
20000000000002

'''
# 수학, 브루트포스, 정수론

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    num = int(input())

    for i in range(2, 1000001):
        if num % i == 0:
            print("NO")
            break

        if i == 1000000:
            print('YES')