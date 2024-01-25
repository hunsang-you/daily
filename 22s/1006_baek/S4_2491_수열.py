'''
9
1 2 2 4 4 5 7 7 2
9
4 1 3 3 2 2 9 2 3
11
1 5 3 6 4 7 1 3 2 9 5
'''

N = int(input())
nums = list(map(int, input().split()))
ans = 1

cnt = 1
for i in range(1, N):       # 오른쪽으로 증가하는 경우
    if nums[i-1] <= nums[i]:
        cnt += 1

    else :
        cnt = 1
    if ans < cnt :
        ans = cnt

cnt = 1             # cnt 초기화
for i in range(1, N):   # 감소하는 경우
    if nums[i-1] >= nums[i]:
        cnt += 1
    else :
        cnt = 1
    if ans < cnt:
        ans = cnt

print(ans)