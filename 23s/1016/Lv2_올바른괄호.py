'''
s	        answer
"()()"	    true
"(())()"	true
")()("	    false
"(()("	    false
'''
def solution(s):
    stack = []
    for i in s:
        if i == '(':        # (는 추가
            stack.append(i)
        else:               # ) 일때
            if len(stack) == 0:
                return False
            else:
                stack.pop()     # (가 존재하고 )라면 (를 하나씩 제거
    if len(stack) > 0 :
        return False
    return True