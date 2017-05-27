class Carculater:

    def plus(self, num1, num2):
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
        return num1 + num2

    def minus(self, num1, num2):
        print('{} - {} = {}'.format(num1, num2, (num1 - num2)))
        return num1 - num2

    def multiply(self, num1, num2):
        print('{} x {} = {}'.format(num1, num2, (num1 * num2)))
        return num1 * num2

    def divided(self, num1, num2):
        print('{} % {} = {}'.format(num1, num2, (num1 // num2)))
        return num1 // num2

    def setup(self):
        while True:
            try:
                num_list = input('계산할 두가지 숫자를 입력하세요 ex)12 53 :')
                split_list = num_list.split()
                num1 = int(split_list[0])
                num2 = int(split_list[1])
                print('첫번째 숫자 : {} , 두번째 숫자 : {}'.format(num1,num2))
            except:
                print('잘못 입력하셨습니다. 다시 입력해 주세요.')
                self.setup()
                return False
            text = input('연산할 문자를 입력하세요 ex) + - * / :   종료하시려면 아무키나 누르세요.')
            if text == '+':
                self.plus(num1, num2)
            elif text == '-':
                self.minus(num1, num2)
            elif text == '*':
                self.multiply(num1, num2)
            elif text == '/':
                self.divided(num1, num2)
            else:
                print('계산기를 종료합니다.')
                break

b = Carculater()
b.setup()