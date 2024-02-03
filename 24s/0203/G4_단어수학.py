'''
2
AAA
AAA

2
GCF
ACDEB

10
A
B
C
D
E
F
G
H
I
J

2
AB
BA
'''
# 그리디

import sys
input = sys.stdin.readline

N = int(input())

word = [input().rstrip() for _ in range(N)]
answer = 0
dic = {}


for i in word:
    cnt = len(i)
    for j in i:
        if j not in dic:
            dic[j] = (10**(cnt-1))

        else:
            dic[j] += (10**(cnt-1))
        cnt -= 1

values = list(dic.values())
values.sort(reverse=True)

number = 9
for i in values:
    answer += i * number
    number -= 1

print(answer)