'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''
N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
lst = list(set(lst))
lst.sort()
lst.sort(key=len)
for i in range(len(lst)):
    print(lst[i])