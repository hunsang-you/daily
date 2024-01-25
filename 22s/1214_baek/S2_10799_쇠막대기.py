'''
()(((()())(())()))(())
(((()(()()))(())()))(()())
'''
lst = list(input())

cnt = 0
stack = []

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')

    else:
        if lst[i-1] == '(':
            stack.pop()
            cnt += len(stack)

        else :
            stack.pop()
            cnt += 1
print(cnt)