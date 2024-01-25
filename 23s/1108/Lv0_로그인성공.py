'''
id_pw	                    db	                                                                            result
["meosseugi", "1234"]	[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]	                    "login"
["programmer01", "15789"]	[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]	"wrong pw"
["rabbit04", "98761"]	[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]	            "fail"
'''


def solution(id_pw, db):
    answer = 'fail'
    for info in db:
        if id_pw[0] in info:
            if id_pw[1] in info:
                answer = 'login'

            elif id_pw[1] not in info:
                answer = 'wrong pw'

    return answer