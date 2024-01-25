'''
4
3
0
4
0

10
1
3
5
4
0
0
7
0
0
6
'''
K = int(input())
stack = []
for _ in range(K):
    num = int(input())
    if num != 0 :
        stack.append(num)

    else:
        stack.pop()

print(sum(stack))