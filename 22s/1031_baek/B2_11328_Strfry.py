'''
4
a a
ab ba
ring gnir
newt twan
'''
N = int(input())

for tc in range(N):
    word1, word2 = list(map(str, input().split()))

    word1 = ''.join(sorted(word1))
    word2 = ''.join(sorted(word2))
    result = 'Possible'

    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i] :
            result = 'Impossible'

    if len(word1) != len(word2):
        result = 'Impossible'

    print(result)
