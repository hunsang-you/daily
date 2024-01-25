'''
6
9
2 7 4 1 5 3
'''

N = int(input())
M = int(input())
number = list(map(int, input().split()))
cnt = 0

number.sort()

l, r = 0, N-1

while l < r:
    if number[l] + number[r] < M :
        l += 1

    elif number[l] + number[r] > M :
        r -= 1

    else :
        cnt += 1
        l += 1
        r -= 1
print(cnt)