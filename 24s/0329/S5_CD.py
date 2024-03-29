'''
3 3
1
2
3
1
2
4
0 0

'''
# 투 포인터, 자료구조, 해시를 이용한 집합과 맵, 이분탐색

import sys
input = sys.stdin.readline

while True:
# 상근, 선영
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    sang = [int(input()) for _ in range(N)]
    sun = [int(input()) for _ in range(M)]

    dic = {}
    ans = 0
    for i in sang:
        if i not in dic:
            dic[i] = 1
    for i in sun:
        if i in dic:
            ans += 1


    print(ans)