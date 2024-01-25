'''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''
# 우선순위큐
# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
#
# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

import sys
import heapq
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(numbers, (-x, x))
    else:
        if len(numbers):
            print(heapq.heappop(numbers)[1])
        else:
            print(0)