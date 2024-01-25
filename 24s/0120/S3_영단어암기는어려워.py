'''
7 4
apple
ant
sand
apple
append
sand
sand

12 5
appearance
append
attendance
swim
swift
swift
swift
mouse
wallet
mouse
ice
age
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
words = {}

for _ in range(N):
    word = input().rstrip()

    if len(word) < M:
        continue

    else:
        if word in words:
            words[word] += 1

        else:
            words[word] = 1

word_lst = sorted(words.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_lst:
    print(i[0])