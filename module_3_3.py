def print_params(a = 1, b = 'строка', c = True):
    print('==========================')
    print(f'a={a}, b={b}, c={c}')

print_params()
print_params(1.25)
print_params(True,18)
print_params(38,'38 попугаев','42')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Первый параметр', 2.5, (1,1,2,3,5,8)]
values_dict = {'a':19,'b':{34,24,1},'c':74}

print_params(*values_list)
print_params(**values_dict)

values_list_2=[True,['Василий','Даниил','Никита']]
print_params(12345,*values_list_2)
print_params(*values_list_2,'Hi!!!!')