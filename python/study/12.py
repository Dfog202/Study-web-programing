# 숫자로 이루어진 4자나 6자로 이루어진 문자열 찾기
def alpha_string46(s):
    if s.isdigit() == True:
        if len(s) == 4 or 6:
            return True
    else:
        return False
