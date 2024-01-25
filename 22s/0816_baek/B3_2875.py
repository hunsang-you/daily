# 대회 or 인턴
N, M, K = map(int, input().split())
cnt = 0
# 최소 여자가 2이상, 남자가 1이상, 인턴십을 갈수있는 사람 이상일 동안
while N >= 2 and M >= 1 and N + M >= K + 3 :
    N -= 2
    M -= 1
    cnt += 1
print(cnt)