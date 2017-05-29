# x부터 시작해서 x씩 증가하는 숫자를 n개 가지는 리스트
def number_generator(x, n):
    num_list = list(range(x, x*n+1, x))
    return num_list
