'''
2
<<BP<A>>Cd-
ThIsIsS3Cr3t
ABC<<DE>F<--
'''
# - : 백스페이스, <, >
T = int(input())
for tc in range(T):
    data = list(input())
    L = len(data)
    word = []
    cursor = []

    for i in range(L):
        if data[i] == '<':
            if len(word) :
                cursor.append(word.pop())

        elif data[i] == '>':
            if len(cursor) :
                word.append(cursor.pop())

        elif data[i] == '-':
            if len(word):
                word.pop()
        else:       # 단어일때
            word.append(data[i])

    cursor.reverse()

    print(*word+cursor, sep="")
