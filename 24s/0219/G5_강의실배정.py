'''
3
1 3
2 4
3 5
'''
# 그리디, 우선순위큐

import sys
import heapq
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    S, T = map(int, input().split())
    time.append([S, T])

time.sort(key=lambda x:(x[0], x[1]))
room = []
heapq.heappush(room, time[0][1])

for i in range(1, N):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))