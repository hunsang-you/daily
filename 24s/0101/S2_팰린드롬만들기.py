'''
abab

abacaba

qwerty

abdfhdyrbdbsdfghjkllkjhgfds
'''

import sys
input = sys.stdin.readline

word = input().rstrip()

L = len(word)

for i in range(L):
    if word[i:] == word[i:][::-1]:
        print(len(word) + i)
        break