'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1
4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0
'''
N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
nation = 0       # 나라번호

# 금메달이 많은 순서로 정렬한다.
lst.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):      # 등수를 알고싶은 나라의 숫자를 grade에 저장
    if lst[i][0] == K :
        nation = i

# print(nation)
#
# 공동순위도 생각
for i in range(N):
    if  lst[nation][1:] == lst[i][1:] :
        print(i+1)
        break

# for _ in lst:
#     print(*_)