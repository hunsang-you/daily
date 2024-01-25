'''
2 1

4 5

3 3
'''

# 패티 A, 치즈 B 최소 1개 이상, 번갈아가면서, A == B + 1
# ans = A + B

A, B = map(int, input().split())

if A > B :
    print (B * 2 + 1)

else:
    print((A-1) * 2 + 1)
