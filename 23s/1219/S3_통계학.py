'''
5
1
3
8
-2
2

1
4000

5
-1
-2
-3
-1
-2

3
0
0
-1
'''
'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이'''
import sys
input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()

# 산술
print(round(sum(numbers)/N))
# 중앙
print(numbers[N//2])

dic = dict()
for i in numbers:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 최빈값 구하기
mnum = max(dic.values())
numarr = []
for i in dic:
    if mnum == dic[i]:
        numarr.append(i)

if len(numarr) > 1:
    print(numarr[1])
else:
    print(numarr[0])


print(max(numbers) - min(numbers))
