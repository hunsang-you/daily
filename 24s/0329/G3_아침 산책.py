'''
5
10111
1 2
2 3
2 4
4 5


'''
import sys
input = sys.stdin.readline

N = int(input())
arr = list(str(input().rstrip()))

graph = [list(map(int, input().split())) for _ in range(N-1)]

print(arr)