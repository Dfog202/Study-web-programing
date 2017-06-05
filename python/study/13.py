# 대문자, 소문자가 혼합된 문자열에 p 와 y의 수가 같으면 True
# 다르면 False, 없으면 True
def numPY(s):
    l = s.upper()
    a = l.count('P')
    b = l.count('Y')
    if a - b == 0:
        return True
    elif a - b != 0:
        return False
    else:
        return True
