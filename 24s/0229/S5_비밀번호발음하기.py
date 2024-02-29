'''
a
tv
ptoui
bontres
zoggax
wiinq
eep
houctuh
end
'''
# 구현, 문자열
# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
import sys
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input().rstrip()
    v_check, c_check = False, False
    cnt = 0

    # end가 나오면 종료
    if password == 'end':
        break

    # 모음 개수
    for i in vowel:
        if i in password:
            cnt += 1

    if cnt < 1:
        print(f'<{password}> is not acceptable.')
        continue

    # 3개 연속인 경우
    for i in range(len(password)-2):
        if (password[i] in vowel) and (password[i+1] in vowel) and (password[i+2] in vowel):
            v_check = True

        elif (password[i] not in vowel) and (password[i+1] not in vowel) and (password[i+2] not in vowel):
            c_check = True

    if v_check == True or c_check == True:
        print(f'<{password}> is not acceptable.')
        continue

    check = False
    # 같은 알파벳이 두개인경우(ee나 oo는 제외)
    for i in range(len(password)-1) :
        if password[i] == password[i+1] :
            if password[i] == 'e' or password[i] == 'o' :
                continue
            else :
                check = True
    if check == True :
        print(f'<{password}> is not acceptable.')
        continue
    #예외를 모두 통과
    print(f'<{password}> is acceptable.')