'''
survey	                                                    choices	                result
["AN", "CF", "MJ", "RT", "NA"]	                            [5, 3, 2, 7, 5]	        "TCMA"
["TR", "RT", "TR"]	                                            [7, 1, 3]	        "RCJA"
'''
'''
매우 비동의	네오형 3점
비동의	네오형 2점
약간 비동의	네오형 1점
모르겠음	어떤 성격 유형도 점수를 얻지 않습니다
약간 동의	어피치형 1점
동의	어피치형 2점
매우 동의	어피치형 3점
1	매우 비동의
2	비동의
3	약간 비동의
4	모르겠음
5	약간 동의
6	동의
7	매우 동의
'''
survey = ["AN", "CF", "MJ", "RT", "NA"]
choice = [5, 3, 2, 7, 5]
def solution(survey, choices):
    answer = ''
    dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}

    for s, c in zip(survey, choices):
        # 3 이하로 선택하면 [0] 번째가 점수 +
        if c < 4 :
            dic[s[0]] += 4 - c

        elif c > 4 :
        # 5 이상으로 선택하면 [1] 번째가 점수 +
            dic[s[1]] += c - 4

    lst = list(dic.items())
    for s in range(0, 8, 2):
        # [s]번째가 [s+1]보다 점수가 크면 붙임
        if lst[s][1] < lst[s+1][1]:
            answer += lst[s+1][0]
        else:
            # [s]번째가 [s+1]보다 점수가 작으면 붙임(단, 사전상으로 앞인것이 오도록)
            answer += lst[s][0]

    return answer



solution(survey, choice)