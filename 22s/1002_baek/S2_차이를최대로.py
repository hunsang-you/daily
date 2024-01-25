'''
6
20 1 15 8 4 10
'''
def backtrack(k):
    if k == N:
        ans.append(sum(abs(nums[temp[i + 1]] - nums[temp[i]]) for i in range(N - 1)))
        return

    for i in range(N):
        if i not in temp:
            temp.append(i)
            backtrack(k+1)
            temp.pop()

N = int(input())
nums = list(map(int, input().split()))

ans = []
temp = []

backtrack(0)

print(max(ans))