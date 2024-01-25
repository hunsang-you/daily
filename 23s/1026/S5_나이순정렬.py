'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''
# 정렬
# 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성

N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append([int(age), name])
members = sorted(members, key=lambda x:x[0])

for i in range(N):
    print(*members[i])