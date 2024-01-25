'''
5 0
-7 -3 -2 5 8
'''
def backtrack(idx, res):
    global cnt
    if idx >= N :
        return

    res += arr[idx]
    if res == S:
        cnt += 1
    backtrack(idx+1, res - arr[idx])
    backtrack(idx+1, res)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
lst = []
cnt = 0

backtrack(0, 0)
print(cnt)