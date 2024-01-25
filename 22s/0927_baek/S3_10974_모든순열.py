'''
3
'''
N = int(input())
lst = []

def func():
    if len(lst) == N:
        print(*lst)
        return

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            func()
            lst.pop()

func()