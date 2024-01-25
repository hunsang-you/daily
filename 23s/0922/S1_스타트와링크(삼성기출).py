'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
'''

# 백트래킹 : 가능한 모든 경우
# n : 사람번호 n==N 일때 종료조건
# dfs (n, if n==N: 종료: 정답처리)
# alist, blist  (if len(alist) == len(blist))
# ans ( min(ans, cal(alist, blist)) 능력치 차이 계산
# 하부호출 #A팀 #B팀
# A팀 -> dfs(n+1, alist+[n], blist)
# B팀 -> dfs(n+1, alist, blist+[n]
import sys

# def cal(alist, blist):
#     asum = bsum = 0
#     for i in range(M):
#         for j in range(M):
#             asum += arr[alist[i]][alist[j]]
#             bsum += arr[blist[i]][blist[j]]
#     return abs(asum-bsum)

def dfs(n, alist, blist):
    global ans
    # 가지치기(한다고 무조건 시간이 줄어드는 것은 아니다)
    if ans == 0 :   # 이미 0이라면 최소값
        return
    # 한팀이 이미 M명 초과인 경우
    if len(alist) > M or len(blist) > M :
        return

    if n == N :
        if len(alist) == len(blist) : # 같은 인원으로 팀구성 시 종료
            # ans = min(ans, cal(alist, blist)) # def cal을 따로 뺏을 시 이용
            asum = bsum = 0
            for i in range(M):
                for j in range(M):
                    asum += arr[alist[i]][alist[j]]
                    bsum += arr[blist[i]][blist[j]]
            ans = min(ans, abs(asum-bsum))
        return

    dfs(n+1, alist+[n], blist)    # A팀 선택
    dfs(n+1, alist, blist+[n])    # B팀 선택

input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

M = N // 2
ans = 100 * M * M #충분히 큰 값

dfs(0, [], [])

print(ans)