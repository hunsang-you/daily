'''
9 8
CCTGGATTG
2 0 1 1

4 2
GATA
1 0 0 1
'''

S, P = map(int, input().split())
word = list(str(input()))
checkList = list(map(int, input().split()))

myList = [0] * 4
checkSecret = 0

result = 0
def addpass(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0] :
            checkSecret += 1

    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1

    elif c == 'G' :
        myList[2] += 1
        if myList[2] == checkList[2] :
            checkSecret += 1

    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def remove(c):
    global checkList, myList, checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1

    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1

    elif c == 'G' :
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1

    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    addpass(word[i])

if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    addpass(word[i])
    remove(word[j])
    if checkSecret == 4:
        result += 1
print(result)