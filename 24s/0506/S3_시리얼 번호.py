'''
5
ABCD
145C
A
A910
Z321

2
Z19
Z20

4
34H2BJS6N
PIM12MD7RCOLWW09
PYF1J14TF
FIPJOTEA5

5
ABCDE
BCDEF
ABCDA
BAAAA
ACAAA

'''
# 정렬

import sys
input = sys.stdin.readline

N = int(input())

def func(n):
    result = 0
    for i in n:
        if i.isdigit():
            result += int(i)
    return result


arr = []
for i in range(N):
    serial = input().rstrip()
    arr.append(serial)


arr.sort(key=lambda x:(len(x), func(x), x))

for i in arr:
    print(i)