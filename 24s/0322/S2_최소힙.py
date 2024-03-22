'''
9
0
12345678
1
2
0
0
0
0
32


'''

import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    number = int(input())
    if number != 0:
        heapq.heappush(heap, number)

    else:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
