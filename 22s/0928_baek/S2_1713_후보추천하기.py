'''
3
9
2 1 4 3 5 6 2 7 2
'''
N = int(input())
V = int(input())        # 추천횟수
vote = list(map(int, input().split()))  # 학생투표
pic = []       # 사진틀
cnt = []        # 각 후보의 추천

for i in range(V):
    if vote[i] in pic:      # 사진틀에 있을때
        for j in range(len(pic)):
            if vote[i] == pic[j] :      # 투표번호와 동일하면 +1 해준다
                cnt[j] += 1

    else :
        if len(pic) >= N :      # 사진틀에 후보가 없는데 사진틀이 꽉찬 상황일 때
            for j in range(N):
                if cnt[j] == min(cnt):      # 추천수가 가장 낮은 cnt[j], pic[j]를 빼주고 새로운 후보를 넣는다.
                    del pic[j]
                    del cnt[j]
                    break

        pic.append(vote[i])     # 새로운 후보를 사진틀에 추가
        cnt.append(1)
    # print(cnt)
    # print(pic)
    # print()
pic.sort()
print(*pic)


