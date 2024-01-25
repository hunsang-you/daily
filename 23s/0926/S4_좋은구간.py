'''
4
1 7 14 10
2

5
4 8 13 24 30
10

5
10 20 30 40 50
30

8
3 7 12 18 25 100 33 1000
59
'''
# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
import sys
input = sys.stdin.readline
L = int(input())
S = list(map(int, input().split()))
S.sort()
N = int(input())
if N in S:
    print(0)

else :
    start = 0
    end = 0

    for num in S:
        if num < N:
            start = num
        elif num > N and end == 0:
            end = num

    start += 1
    end -= 1
    print((N-start) * (end-N+1) + (end-N))
