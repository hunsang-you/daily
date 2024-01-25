'''
5
3 4
1 1
1 -1
2 2
3 3
'''
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

N=int(input())
li=[]
for i in range(N):
    [a, b] = map(int, input().split())
    li.append([a, b])
li.sort()
for i in li:
    print(i[0], i[1])