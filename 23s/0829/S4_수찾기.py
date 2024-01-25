'''
5
4 1 5 2 3
5
1 3 7 9 5
'''

def func(target, data):
    s = 0
    e = N-1

    while s <= e:
        mid = (s+e) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            s = mid + 1
        else :
            e = mid - 1
    return 0




N = int(input())
N_num = list(map(int, input().split()))
N_num.sort()

M = int(input())
M_num = list(map(int, input().split()))

for i in M_num:
    if func(i, N_num):
        print(1)
    else:
        print(0)