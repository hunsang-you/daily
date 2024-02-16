'''
3
000
010
'''
# 그리디

import sys
input = sys.stdin.readline

N = int(input())

now = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def check(lst, cnt):
    for i in range(1, N-1):
        if lst[i-1] != target[i-1]:
            cnt += 1

            for j in range(i-1, i+2):
                lst[j] = not lst[j]

    if lst[N-1] != target[N-1]:
        cnt += 1
        lst[N-2] = 1 - lst[N-2]
        lst[N-1] = 1 - lst[N-1]

    if lst == target:
        return cnt

    else :
        return -1

# 첫번째 스위치를 먼저 누르고 시작하는 경우를 생각
on_now = now.copy()
on_now[0] = 1 - now[0]
on_now[1] = 1 - now[1]

if now == target:
    print(0)

else:
    answer = check(now, 0)

    if answer != -1:
        print(answer)

    else:
        answer = check(on_now, 1)
        if answer != -1:
            print(answer)
        else:
            print(-1)

