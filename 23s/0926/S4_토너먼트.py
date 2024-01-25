'''
16 1 2

16 8 9

1000 20 31

65536 1000 35000

60000 101 891
'''
import sys
input = sys.stdin.readline
N, Kim, Im = map(int, input().split())


ans = 0

while Kim != Im :
    Kim -= Kim // 2
    Im -= Im // 2
    ans += 1

print(ans)