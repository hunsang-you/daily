'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
'''

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))
dic = {}
for i in nums :
    if i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1

for i in lst:
    if i in dic :
        print(dic[i], end=' ')
    else:
        print(0, end=' ')

# print(dic)

