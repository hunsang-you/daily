'''
5 3.59
4 A+
3 B+
3 C+
1 D0
3

3 4.44
5 A+
4 A+
1

5 2.54
3 B+
2 B0
2 C+
2 C0
1

5 3.60
4 A+
3 B+
3 C+
1 D0
3
'''
# 수강 과목수 N, 최소 평균 평점 X
import sys
input = sys.stdin.readline
import math

N, X = map(str, input().split())
grade = [0] * int(N)
ans = ''
for i in range(int(N)-1):
    C, G = map(str, input().split())
    temp = 0
    temp += int(C)
    if G == 'A+' :
        G = 4.50
    elif G == 'A0':
        G = 4.00
    elif G == 'B+':
        G = 3.50
    elif G == 'B0':
        G = 3.00
    elif G == 'C+':
        G = 2.50
    elif G == 'C0':
        G = 2.00
    elif G == 'D+':
        G = 1.50
    elif G == 'D0':
        G = 1.00
    else :
        G = 0.00
    grade[i] = [int(C), G]

grade[-1] = [int(input())]

temp1 = 0   # 학점 총합
temp2 = 0   # 학점 * 평점의 합
# [[4, 4.5], [3, 3.5], [3, 2.5], [1, 1.0], [3]]
for i in grade:
    temp1 += i[0]
    if len(i) == 2:
        temp2 += i[0] * i[1]

maxC = float(X) * temp1     # 전체 점수
diff = (maxC - temp2) / grade[-1][0]  # 전체점수 - 학점*평점합 / 나머지

if 4.0 < diff <= 4.5 :
    ans = 'A+'
elif 3.5 < diff <= 4.0:
    ans = 'A0'
elif 3.0 < diff <= 3.5:
    ans = 'B+'
elif 2.5 < diff <= 3.0:
    ans = 'B0'
elif 2.0 < diff <= 2.5:
    ans = 'C+'
elif 1.5 < diff <= 2.0:
    ans = 'C0'
elif 1.0 < diff <= 1.5:
    ans = 'D+'
elif 0.0 < diff <= 1.0:
    ans = 'D0'
elif 0.0 >= diff :
    ans = 'F'
else :
    ans = 'impossible'

print(maxC, diff, temp1, temp2)
print(ans)