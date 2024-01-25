'''
3, 7 -> 15
'''

L, R = map(int, input().split())

lst = []
sumV = 0
for i in range(R+1):
    for j in range(i):
        lst.append(i)

for i in range(L-1, R):
    sumV += lst[i]


print(sumV)