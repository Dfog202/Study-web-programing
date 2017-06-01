'''number의 각 자릿수를 더해서 return하세요'''
def sum_digit(number):
    make_str = str(number)
    li = list(make_str)
    j = 0
    
    for i in li:
        j += int(i)
    return j
                                    
