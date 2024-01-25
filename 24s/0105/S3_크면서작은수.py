'''
156

330

27711
'''
# 백트래킹
from itertools import permutations

N = input()

numbers = list(permutations(N, len(N)))

numbers.sort()
answer = []
for i in numbers:
    answer.append("".join(i))

temp = -1
for i in range(len(answer)):
    if int(answer[i]) > int(N):
        temp = i
        break

if temp != -1:
    print(answer[temp])

else:
    print(0)