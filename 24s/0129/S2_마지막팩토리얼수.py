'''
5
'''
from math import factorial

N = (factorial(int(input())))
fac = list(str(N))

for i in fac[::-1]:
    if i != '0':
        print(i)
        break
