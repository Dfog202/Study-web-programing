def print_args(*args):
    print(args)

def print_kwargs(**kwargs):
    print(kwargs)

print_args('python', 'ruby', 'java')
print('')
print_args(language = 'python', ide='pycham')
print('')
print_kwargs(language = 'python', ide = 'pycham')
print('')


