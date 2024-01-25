'''
s	                            return
"3people unFollowed me"	    "3people Unfollowed Me"
"for the last week"	        "For The Last Week"
'''
def solution(s):
    answer = ''
    new=s.split(' ')
    for i in range(len(new)):
        new[i]=new[i].capitalize()
    answer=' '.join(new)
    return answer

solution("3people unFollowed me")