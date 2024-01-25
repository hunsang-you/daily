# 수 정렬하기
N = int(input())
lst = []
for i in range(N):
    num = int(input())
    lst.append(num)


lst = sorted(lst)

for j in range(N):
    print(lst[j])