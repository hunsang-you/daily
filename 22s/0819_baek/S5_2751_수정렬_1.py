# 수 정렬하기
# 백준의 시간제한 2초에 시간초과가 난다.
# 문자를 입력받을 때
# import sys;  sys.stdin.readline()으로 읽어야 시간초과가 나지 않는다.

N = int(input())                                    # 숫자의 갯수


lst = []
for i in range(N):                                  # 입력한 숫자를 lst에 추가
    num = int(input())
    lst.append(num)

for i in range(len(lst)):                               # 숫자를 오름차순 정렬
    idx=0
    for j in range(1, N):
        if lst[idx] > lst[j]:
            lst[idx], lst[j] = lst[j], lst[idx]
        idx += 1


# print(lst)
for num in lst:
    print(num)