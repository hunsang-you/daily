'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3

10 5
3 -2 -4 -9 0 3 7 13 8 -3
'''
# 누적합, 투 포인터, 슬라이딩 윈도우

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tem = list(map(int, input().split()))
part = sum(tem[:K])
result = [part]

for i in range(0, len(tem)-K):
    part = part - tem[i] + tem[i+K]
    result.append(part)

print(max(result))