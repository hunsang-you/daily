N = int(input())

lst = []
for word in range(N):
    word = list(input())
    lst.append(word)

# 단어를 길이에 따라 정렬하기
for i in range(N):
    idx= 0
    for j in range(1, len(lst)):
        if len(lst[idx]) > len(lst[j]):
            lst[idx], lst[j] = lst[j], lst[idx]
        idx += 1

# 중복된 단어를 제외한 단어 리스트
set_lst = []
for i in lst :
    if i not in set_lst:
        set_lst.append(i)


for i in range(1, len(set_lst)):
    if len(set_lst[i-1]) == len(set_lst[i]) and set_lst[i-1] > set_lst[i] :           # 양옆에 있는 단어의 길이가 같다면
        set_lst[i-1], set_lst[i] = set_lst[i], set_lst[i-1]                           # 첫글자에 따라 오름차순 정렬


print(set_lst)

