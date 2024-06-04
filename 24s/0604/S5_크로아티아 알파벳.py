'''
ljes=njak

ddz=z=

nljj

c=c=

dz=ak

'''
# 구현,문자열

import sys
input = sys.stdin.readline

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()

for i in croatia :
    word = word.replace(i, '*')
print(len(word))