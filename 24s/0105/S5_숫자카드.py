'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''
# 이분탐색
import sys
input = sys.stdin.readline

N = int(input())
numbers1 = list(map(int, input().split()))
numbers1.sort()
M = int(input())
numbers2 = list(map(int, input().split()))


for i in range(N+(M-N)):
    L, R = 0, N-1
    check = False

    while L <= R:
        mid = (L + R) // 2
        if numbers1[mid] > numbers2[i]:
            R = mid - 1
        elif numbers1[mid] < numbers2[i]:
            L = mid + 1

        else:
            check = True
            break

    if check == True:
        print(1, end=' ')
    else:
        print(0, end=' ')


