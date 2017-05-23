from main import *
#여기서 실행
class Study:
    def __init__(self, name, exp=0):
        self.name = name
        self.exp = exp

    def random_study(self):
        if l.exp % 3 == 0:
            l.study_html()
        elif l.exp % 3 == 1:
            l.study_py()
        else:
            print('함정카드 발동!! 오늘은 공부가 눈에 안들어온다 경험치 -1')
            l.exp -= 1

    def study_html(self):
        l.exp += 22
        print('HTML을 공부했다! 경험치가 {}되었다.'.format(self.exp))

    def study_py(self):
        l.exp += 23
        print('PYTHON을 공부했다! 익숙해지는 기분이다 현재 경험치 {}!'.format(self.exp))

if __name__ == '__main__':
    l = Study(input('이름을 입력해 주세욥!! : '))
    Main.select_main(l)
