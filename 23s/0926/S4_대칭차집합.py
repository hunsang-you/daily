'''
3 5
1 2 4
2 3 4 5 6

'''
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
Alist = set(map(int, input().split()))
Blist = set(map(int, input().split()))

print(len(Alist - Blist) + len(Blist - Alist))