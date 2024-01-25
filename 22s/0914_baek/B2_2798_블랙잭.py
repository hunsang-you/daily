'''
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295
'''
N, M = map(int, input().split())        # N : 카드의 개수,  M : 합의 최대
cards = list(map(int, input().split()))

result = 0             # 3장의 합

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cards[i] + cards[j] + cards[k] > M :
                continue
            else :
                result = max(result, cards[i]+cards[j]+cards[k])

print(result)