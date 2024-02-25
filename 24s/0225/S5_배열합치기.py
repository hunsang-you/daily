'''
2 2
3 5
2 9

2 1
4 7
1

4 3
2 3 5 9
1 4 7

'''
# 투포인터
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
new = []
a_id, b_id = 0, 0

while a_id !=(len(arr)) or b_id != (len(brr)):
    if a_id == len(arr):
        new.append(brr[b_id])
        b_id += 1

    elif b_id == len(brr):
        new.append(arr[a_id])
        a_id += 1

    else:

        if arr[a_id] < brr[b_id]:
            new.append(arr[a_id])
            a_id += 1
        elif arr[a_id] > brr[b_id]:
            new.append(brr[b_id])
            b_id += 1


print(*new)