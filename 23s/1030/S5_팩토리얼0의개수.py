'''
10

3
'''

from math import factorial

N = int(input())

num = factorial(N)
cnt = 0
for i in str(num)[::-1]:
    if i != '0':
        break
    if i == '0':
        cnt += 1


print(cnt)