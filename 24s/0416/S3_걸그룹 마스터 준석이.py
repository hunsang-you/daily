'''
3 4
twice
9
jihyo
dahyeon
mina
momo
chaeyoung
jeongyeon
tzuyu
sana
nayeon
blackpink
4
jisu
lisa
rose
jenny
redvelvet
5
wendy
irene
seulgi
yeri
joy
sana
1
wendy
1
twice
0
rose
1

'''
# 자료구조, 해시를 사용한 집합와 맵

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for i in range(N):
    team = input().rstrip()
    total = int(input())
    for j in range(total):
        name = input().rstrip()
        dic[name] = team

for i in range(M):
    quiz = input().rstrip()
    num = int(input())
    if num == 1:
        print(dic[quiz])

    else:
        temp = []
        for k, v in dic.items():
            if v == quiz:
                temp.append(k)
        temp.sort()
        for j in range(len(temp)):
            print(temp[j])
