from user import Study
# 코드 꼬임 ㅋㅋㅋㅋ user에서 실행해야함!!!
class Main:

    def select_main(self):
        while True:
            choice = input('{}? 오늘은 뭐할래?\n  1: 공부, 2: 게임, 0: 재미없엉 끌래!\n    Input : '.format(self.name))
            if choice == '0':
                print("미워도 다시한번 ㅠ 또봐 {}.".format(l.name))
                break
            elif choice == '1':
                if self.exp <= 100:
                    self.random_study()
                else:
                    print('경험치 초과: {}  이제 그만... 고생했어 잘가!'.format(self.exp))
                    break
            elif choice == '2':
                print('미안 아직 안만들었어 공부는 어때?')
            else:
                print('정확한 숫자를 입력해 주세요ㅠ')
            print('-----------------------')


if __name__ == '__main__':
    select_main()