'''
aabbcc
xxyybb
'''
word1 = input()
word2 = input()

word1_lst = [0] * 26
word2_lst = [0] * 26

for alp in word1:           # word1의 alp 수
    word1_lst[ord(alp) - 97] += 1

for alp in word2:           # word2의 alp 수
    word2_lst[ord(alp) - 97] += 1

result = 0
for i in range(26):
    result += abs(word1_lst[i] - word2_lst[i])      # 알파벳 개수차이만큼 더하기


# print(word1_lst)
# print(word2_lst)
print(result)