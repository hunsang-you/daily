'''
s	                            result
"one4seveneight"	             1478
"23four5six7"	                234567
"2three45sixseven"	            234567
"123"	                         123
'''
s = "one4seveneight"
def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

    for alp in num:
        if alp in s:
            idx = str(num.index(alp))
            s = s.replace(alp, idx)
    return int(s)


solution(s)