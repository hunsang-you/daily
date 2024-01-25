'''
2
1 1
1 2
2 1
2 2
2 2
3 3
4 4
5 5
'''
# 네 점이 주어졌을 때, 네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

t=int(input())
square=[]
tmp=0

def distance(n1,n2):
    return abs((n2[0]-n1[0])**2+abs(n2[1]-n1[1])**2)

for _ in range(t):
    square=[]
    for _ in range(4):
        a,b=map(int,input().split())
        square.append([a,b])
    square=sorted(square) # 사각형 만들기 위해 정렬

    ## [0,0] * 4 인 점의 케이스 제외
    for dot in square:
        if dot==[0,0]:
            tmp+=1
    if tmp==4:
        print(0)
        tmp=0
    # 두 변의 길이가 같고, 두 대각선의 길이가 같으면
    elif distance(square[0],square[1])==distance(square[0],square[2])==distance(square[1],square[3]) and distance(square[1],square[2])==distance(square[0],square[3]):
        print(1)
    else:
        print(0)