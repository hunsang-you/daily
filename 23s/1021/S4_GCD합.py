'''
3
4 10 20 30 40
3 7 5 12
3 125 15 25
'''

import sys
input = sys.stdin.readline
import math
n=int(input())

for i in range(n):
    arr=list(map(int, input().split()))
    total=0
    for j in range(1,len(arr)):
        for k in range(j+1,len(arr)):
            total+=math.gcd(arr[j],arr[k])

    print(total)