# 공
M = int(input())
cup = [0, 1, 0, 0]              # 컵의 번호와 인덱스를 맞춰주기 위해 [0] 을 추가, 1은 공이 있는 자리

for i in range(M):
    X, Y = map(int, input().split())
    cup[X], cup[Y] = cup[Y], cup[X]         # 컵의 위치를 서로 교환


print(cup.index(1))