'''
1000
3

2000000000
100

23442
75

428392
17
'''
import sys
input = sys.stdin.readline

N = int(input())
F = int(input())
temp = N // 100
ans = temp * 100

while ans % F != 0:
    ans += 1
print(str(ans)[-2:])