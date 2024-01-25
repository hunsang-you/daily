'''
9
5 12 7 10 9 1 2 3 11
13
'''
N = int(input())
arr = list(map(int, input().split()))
arr.sort()          # [1, 2, 3, 5, 7, 9, 10, 11, 12]
X = int(input())
cnt = 0
# 2중 for문을 이용한 방법은 시간초과
# for i in range(N):
#     for j in range(i+1, N):
#         if arr[i] + arr[j] == X :
#             cnt += 1


left = 0
right = len(arr) - 1

while left < right :
    if arr[left] + arr[right] == X :
        cnt += 1
    if arr[left] + arr[right] < X :
        left += 1
        continue
    right -= 1

print(cnt)