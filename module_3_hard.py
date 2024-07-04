def calculate_structure_sum(same_args):
    t=type(same_args)
    res=0
    if t in (int, float, complex):
        return same_args
    elif t == str:
        return len(same_args)
    elif t == bool:
        if same_args:
            return 1
        else:
            return 0
    elif t in (list, tuple, set):
        for i in same_args:
            res+=calculate_structure_sum(i)
        return res
    else:                   #последний вариант еслт type(same_args) == 'dict
        for i in same_args:
            res+=calculate_structure_sum(i)+calculate_structure_sum(same_args[i])
        return res

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
