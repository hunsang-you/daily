'''
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
'''
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    rec = [list(map(int, input().split())) for _ in range(N)]
    rec.sort()
    result = 1
    check = rec[0][1]
    for i in range(1, N):
        if check > rec[i][1]:
            result += 1
            check = rec[i][1]
    print(result)