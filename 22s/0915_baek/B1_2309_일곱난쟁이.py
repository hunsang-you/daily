'''
20
7
23
19
10
15
25
8
13
'''
lst = []
tmp1 = 0
tmp2 = 0



for i in range(9):
    height = int(input())
    lst.append(height)


tot_height = sum(lst)

fake = tot_height - 100

for i in range(len(lst)) :
    for j in range(1, len(lst)):
        if lst[i] + lst[j] == fake:
            tmp1 = lst[i]
            tmp2 = lst[j]

lst.remove(tmp1)
lst.remove(tmp2)


sorted_lst = sorted(lst)
for i in range(7):
    print(sorted_lst[i])