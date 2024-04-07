'''
4 3
0
2 1 2
1 3
3 2 3 4

4 1
1 1
4 1 2 3 4

4 1
0
4 1 2 3 4

4 5
1 1
1 1
1 2
1 3
1 4
2 4 1

10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4

8 5
3 1 2 7
2 3 4
1 5
2 5 6
2 6 8
1 8

3 4
1 3
1 1
1 2
2 1 2
3 1 2 3

'''
# 자료구조, 그래프 이론, 탐색, 분리집합

import sys
input = sys.stdin.readline

# 사람 수, 파티 수
N, M = map(int, input().split())

knowlst = list(map(int, input().split()))
party = []

# 아는사람이 없을경우, 파티의 수만큼 거짓말
if knowlst[0] == 0:
    print(M)

else:
    knowlst = set(knowlst[1:])
    for _ in range(M):
        people = list(map(int, input().split()))
        party.append(set(people[1:]))

    for _ in range(M):
        for i in party:
            if i & knowlst:
                knowlst = knowlst.union(i)

    # 최대로 거짓말 할수 있는 경우는 파티의 수에서 knowlst 사람이 있을경우마다 -1
    ans = M
    for i in party:
        if i & knowlst:
            ans -= 1

    print(ans)
