import sys

N = int(input())

lst = []

for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)

sorted_num = sorted(lst)


for i in range(N):
    print(sorted_num[i])