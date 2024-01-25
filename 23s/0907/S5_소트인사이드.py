'''
2143

999998999

61423

500613009
'''
N = list(map(int, input()))

for i in range(len(N)-1):
    for j in range(len(N)-1):
        if N[j] < N[j+1] :
            temp = N[j]
            N[j] = N[j+1]
            N[j+1] = temp

for i in range(len(N)):
    print(N[i], end='')