'''
5
1 2 1 4 6
8
12 20 1 3 4 4 11 1
6
10 8 8 6 4 3
'''
N = int(input())
road = list(map(int, input().split()))
# 같은 높이가 나와도 오르막길이 멈춘다-> 계속해서 차이가 나야한다

up = 0      #  오른쪽 - 왼쪽의 차
lst = []        # 차이가 들어갈 리스트
for i in range(N-1):
    if road[i] < road[i+1] :    # 왼쪽 < 오른쪽 (오르막길)이라면
        up += road[i+1] - road[i]    # 그 차이를 변수에 더한다
    else :
        lst.append(up)      # 오르막길이 끊기면 그때까지의 차를 리스트에 추가
        up = 0      # 초기화
lst.append(up)      # 마지막이 오르막길의 끝일 경우 추가

lst.sort(reverse=True)      # 높이 내림차순 정렬

if len(lst) > 0 :   # 오르막길이 존재한다면
    print(lst[0])

else :      # 오르막길이 없는경우
    print(0)
