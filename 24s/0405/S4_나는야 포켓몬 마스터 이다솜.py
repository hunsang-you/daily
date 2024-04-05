'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

'''
# 자료구조, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}

for i in range(1, N+1):
    name = input().rstrip()
    dic[name] = i
    dic[i] = name

for i in range(M):
    name = input().rstrip()
    if name.isdigit():
        print(dic[int(name)])

    else:
        print(dic[name])