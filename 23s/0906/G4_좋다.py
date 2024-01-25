'''
10
1 2 3 4 5 6 7 8 9 10
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0



for i in range(N):
    target = arr[i]
    l, r = 0, N - 1
    while l < r :
        if arr[l] + arr[r] == target :
            if l != i and r != i :
                cnt += 1

                break
            elif l == i :
                l += 1
            elif r == i :
                r -= 1

        elif arr[l] + arr[r] < target :
            l += 1

        else :
            r -= 1

print(cnt)