'''
3
8 5
1 100
3 5

3
1 100
8 5
3 5

1
123 45

8
222 117
176 92
287 6
284 81
221 96
263 96
188 40
225 1

6
65 281
272 145
233 175
229 12
99 88
142 159

8
161 36
248 93
233 13
241 122
285 91
260 25
221 14
233 42

3
213 295
153 24
15 233

8
44 11
116 73
121 54
49 232
69 136
159 242
109 172
28 31

6
100 1
100 1
100 1
100 1
100 1
100 1

'''
# 브루트포스, 백트래킹

import sys
input = sys.stdin.readline

N = int(input())

eggs = [list(map(int, input().split())) for _ in range(N)]

def DFS(n, cnt):
    global ans
    # 남은 횟수 모두깨도 ans가 갱신되지 않는 경우        ((N-n) * 2) 의 경우 가지치기
    if ans >= (cnt+(N-n)*2):
        return

    if n == N :     # 모든 계란을 손에 들고 부딪히기 완료
        ans = max(ans, cnt)
        return

    if eggs[n][0] <= 0:     # 현재 계란이 깨진경우 => 다음계란으로 넘어가기
        DFS(n+1, cnt)

    else:                   # 현재 계란이 안깨진 상태
        flag = False        # 한번도 안부딪혔다면 다음계란으로 넘어가야함
        for j in range(N):
            if n == j or eggs[j][0] <= 0:       # j가 현재상태의 계란이거나 부딪힐 계란의 내구도가 없으면 넘어감
                continue
            flag = True
            eggs[n][0] -= eggs[j][1]
            eggs[j][0] -= eggs[n][1]
            DFS(n+1, cnt+int(eggs[n][0] <= 0) + int(eggs[j][0] <= 0))       # 현재 계란과 부딪힌계란 두개의 상태에 따라 1또는 2가 추가
            eggs[n][0] += eggs[j][1]                                        # 원상복구
            eggs[j][0] += eggs[n][1]

        if flag == False:       # 계란이 한번도 안부딪혔다면
            DFS(n+1, cnt)

ans = 0
# 계란 Index, 깨진계란 개수
DFS(0, 0)
print(ans)