def hide_numbers(s):
    # 맨 뒷자리 4자리를 제외한 나머지를 "*"으로 바꿔야 합니다.
    return '*' * (len(s)-4) + s[-4:]
