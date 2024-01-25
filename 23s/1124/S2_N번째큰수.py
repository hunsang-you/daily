'''
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
'''

import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(queue) < N: # heap의 크기를 n개로 유지
            heapq.heappush(queue, number)
        else:
            if queue[0] < number:
                heapq.heappop(queue)
                heapq.heappush(queue, number)
print(queue[0])

