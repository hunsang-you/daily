'''
예제	dartResult	answer	                설명
1	1S2D*3T     	37	                11 * 2 + 22 * 2 + 33
2	1D2S#10S	    9	                12 + 21 * (-1) + 101
3	1D2S0T	        3	                12 + 21 + 03
4	1S*2T*3S	    23                 	11 * 2 * 2 + 23 * 2 + 31
5	1D#2S*3S	    5               	12 * (-1) * 2 + 21 * 2 + 31
6	1T2D3D#	        -4              	13 + 22 + 32 * (-1)
7	1D2S3T*     	59	                12 + 21 * 2 + 33 * 2
'''
'''
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.
'''

dartResult = '1D2S#10S'
def solution(dartResult):
    dartResult = dartResult + 'A'
    score = 0
    oper = []
    for i in range(len(dartResult)):
        # 숫자점수
        if dartResult[i].isnumeric() :
            # 두자리 점수일 경우를 생각해야 함
            if dartResult[i].isnumeric() == dartResult[i+1].isnumeric():
                score += int(dartResult[i] + dartResult[i+1])

            else:
                score += int(dartResult[i])
            continue

        else:
            if dartResult[i] == 'S':
                oper.append(score)
            elif dartResult[i] == 'D':
                oper.append(score ** 2)

            elif dartResult[i] == 'T':
                oper.append(score ** 3)

            elif dartResult[i] == '*':
                # 스타상일때 한판만했다면 첫판만 두배, 아니면 전판 현재판 두배
                if len(oper) > 1:
                    oper[-1] *= 2
                    oper[-2] *= 2

                else:
                    oper[-1] *= 2
            elif dartResult[i] == '#':
                # 아차상일때 현재 판에 -1배
                oper[-1] *= -1

            score = 0       # 점수 초기화

    return sum(oper)


solution(dartResult)