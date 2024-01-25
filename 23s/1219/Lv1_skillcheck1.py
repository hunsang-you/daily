'''
s	        n       	result
"AB"    	1	        "BC"
"z"	        1       	"a"
"a B z"	    4	        "e F d"
'''

print(ord('A'), ord('Z'), ord('a'), ord('z'))
def solution(s, n):
    lower_alp = 'abcdefghijklmnopqrstuvwxyz'
    upper_alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    answer = ''

    for i in s:
        if i == " ":
            answer += " "
        elif i.islower() == True:
            temp = lower_alp.find(i) + n
            answer += lower_alp[temp % 26]

        else:
            temp = upper_alp.find(i) + n
            answer += upper_alp[temp % 26]

    return answer

solution('AB', 1)
solution('z', 1)
solution('a B z', 4)