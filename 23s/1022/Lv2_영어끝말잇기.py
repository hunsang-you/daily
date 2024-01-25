'''
n	words                                                                                                                                                                result
3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	                                                                                    [3,3]
5	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]	[0,0]
2	["hello", "one", "even", "never", "now", "world", "draw"]	                                                                                                        [1,3]
'''
# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다.
# [번호, 차례] 형태


def solution(n, words):
    answer = [0, 0]
    used = []
    turn = -1
    while words:
        word = words.pop(0)
        turn += 1
        if len(used) == 0:
            used.append(word)
        else:
            if (word in used) or (used[-1][-1] != word[0]):
                answer[0] = turn % n + 1
                answer[1] = turn // n + 1
                return answer
            elif word not in used:
                used.append(word)
    return answer



solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])