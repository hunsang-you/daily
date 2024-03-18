'''
55-50+40

10+20+30+40

00009-00009

'''
# 수학, 그리디, 문자열, 파싱

import sys
input = sys.stdin.readline

eq = list(input().rstrip().split('-'))

numbers = []

for i in eq:
    part = 0
    temp = i.split('+')
    for j in temp:
        part += int(j)
    numbers.append(part)

ans = numbers[0]

for i in numbers[1:]:
    ans -= i

print(ans)
