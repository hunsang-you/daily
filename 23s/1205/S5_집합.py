'''
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
'''
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
input = sys.stdin.readline
M = int(input())
S = set()
for i in range(M):
    oper = input().split()

    if len(oper) == 1:
        if oper[0] == 'all':
            S = set(range(1, 21))
        elif oper[0] == 'empty':
            S = set()

    else:
        if oper[0] == 'add':
            S.add(int(oper[1]))

        elif oper[0] == 'remove':
            if int(oper[1]) in S:
                S.remove(int(oper[1]))

        elif oper[0] == 'check':
            if int(oper[1]) in S:
                print(1)
            else:
                print(0)

        elif oper[0] == 'toggle':
            if int(oper[1]) in S:
                S.remove(int(oper[1]))
            else:
                S.add(int(oper[1]))