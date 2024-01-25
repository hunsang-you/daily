'''
9
5 12 7 10 9 1 2 3 11
13
'''
N = int(input())
nums = list(map(int, input().split()))
X = int(input())
cnt = 0

L, R = 0, N-1

nums.sort()

while L < R :
    if nums[L] + nums[R] == X :
        cnt += 1

    if nums[L] + nums[R] < X :
        L += 1
        continue
    R -= 1
print(cnt)