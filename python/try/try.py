import random

정규표현식으로 검사했을때 일치하는 패턴이 없을 경우
NotMatchedException을 정의
Exception을 상속
__init__ 초기화 매소드에 패턴문자열과 소스문자열을 받도록 함
__str__ 멤소드가 일치하는 결과가 없다는 문자열을 리턴하도록 함.

패턴문자열과 소스문자열을 매개변수로 갖는 search_from_source함수를 정의하고,


re.search에 소스 문자열을 전달했을 때 MatchObject를 찾지 못하면 NotMatchedException을 발생시킴
try~except 구문에서 위 함수를 실행해 예외를 발생
try~except의 구문에서 위 함수를 실행해 예외를 발생
위 구문에 else절을 추가해서 예외가 발생하지 않았을 경우의 검색결과를 출력
위 구문에 finally절을 추가해서 프로그램이 끝낫음을 출력

class NotMatchedException(Exception):
    # pattern, source를 받아 매치되지 않았음을 알려주는
    def __init__(self, pattrn_string, source_string)
        self.pattrn_string = pattrn_string
        self.source_string = source_string

]
    def __str__(self):
        return 'Pattern "{}" is not matched in source "{}"'.format(
            self.pattrn_string,
            self.source_string,
        )

def search_from_source(pattern_string, source_string):
    m = re.search(pattern=pattern_string, source_string)
    if m:
        return m
    raise NotMatchedException(pattern_string, source_string)




try:
    source = 'Lux, the Lady of Luminocity'
    pattern_string = r'L\w{3}\b'
    m = search_from source(pattern_string, source)
except NotMatchedException as e:
    print(e)
else:
    print()
finally:
    print('search end---')