'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
# 그리디
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표
#  각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다
import sys
input = sys.stdin.readline

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time = sorted(time, key=lambda x:(x[1], x[0]))

cnt = 1
end = time[0][1]
for i in range(1, N):
    if time[i][0] >= end:
        cnt += 1
        end = time[i][1]

print(cnt)