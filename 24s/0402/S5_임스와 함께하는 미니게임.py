'''
7 Y
lms0806
lms0806
exponentiale
lms0806
jthis
lms0806
leo020630

12 F
lms0806
powergee
skeep194
lms0806
tony9402
lms0806
wider93
lms0806
mageek2guanaah
lms0806
jthis
lms0806

12 O
lms0806
mageek2guanaah
jthis
lms0806
exponentiale
lms0806
leo020630
lms0806
powergee
lms0806
skeep194
lms0806

'''
# 자료구조, 문자열, 해시를 사용한 집합과 맵

import sys
input = sys.stdin.readline

N, game = map(str, input().rstrip().split())

user = set()
for _ in range(int(N)):
    id = input().rstrip()
    user.add(id)

if game == 'Y':
    print(len(user))
elif game == 'F':
    print(len(user)// 2)

else:
    print(len(user)// 3)