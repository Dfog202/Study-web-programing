# seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환
def findKim(seoul):
    kimIdx = seoul.index('Kim')
    return "김서방은 {}에 있다".format(kimIdx)
