'''
4
2 3 1
5 2 4 1

4
3 3 4
1 1 1 1

'''
# 그리디 알고리즘

import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = oil[0]     # 가장 싼 가격의 주유소

ans = oil[0] * road[0]
for i in range(1, N-1):
    # 다음 주유소의 가격이 제일 싸다면 갱신하고 나머지 거리를 모두 사서감
    if oil[i] < min_oil:
        min_oil = oil[i]
    ans += min_oil * road[i]

print(ans)