'''
1 3
1 2 3
1 3 5
1 4 6

2 4
1 1 4
2 2 5
1 3 7
1 5 8
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [[0] for _ in range(N)]

for _ in range(M):
    k, s, e = list(map(int, input().split()))
    if table[k-1] == [0]:
        table[k-1] = [s, e]
        print("YES")
    elif table[k-1] != [0]:
        if table[k-1][1] > s:
            print("NO")

        elif table[k-1][1] <= s:
            table[k-1] = [s, e]
            print("YES")