# 덩치
# 부르트 포스
N = int(input())        # 사람 수
size = []
for tc in range(N):
    weight, height = map(int, input().split())
    size.append((weight, height))



# 몸무게 순으로 오름차순 정렬
#
# for i in range(1, N):
#     for j in range(N):
#         if size[j-1][0] > size[j][0] :
#             size[j-1], size[j] = size[j], size[j-1]

for i in size:
    rank = 1                                        # 등수 초기화
    for j in size:                                  # 몸무게와 키가 둘다 작으면 rank + 1
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1

    print(rank, end = " ")

print()
print(size)