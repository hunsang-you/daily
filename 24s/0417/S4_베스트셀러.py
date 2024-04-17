'''
5
top
top
top
top
kimtop

9
table
chair
table
table
lamp
door
lamp
table
chair

6
a
a
a
b
b
b

6
a
a
a
b
b
b

8
icecream
peanuts
peanuts
chocolate
candy
chocolate
icecream
apple

1
soul

'''
# 자료구조, 문자열, 정렬, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N):
    name = input().rstrip()
    if name not in dic:
        dic[name] = 1

    else:
        dic[name] += 1

best = max(dic.values())
seller = []
for k, v in dic.items():
    if v == best:
        seller.append(k)

seller.sort()

print(seller[0])