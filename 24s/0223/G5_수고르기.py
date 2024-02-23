'''
3 3
1
5
3
'''
# 정렬, 투포인터

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
answer = 2e9
left, right = 0, 0

# left가 right보다 작고 right가 N보다 작을 동안 반복
while left <= right and right < N:
        temp = numbers[right] - numbers[left]       # 두 수의 차
        # 두수의 차가 M보다 작으면 오른쪽을 증가
        if temp < M:
            right += 1

        # 두 수의 차이가 M보다 크면 그중 가장 작은것을 확인
        else:
            answer = min(answer, temp)
            left += 1

print(answer)
